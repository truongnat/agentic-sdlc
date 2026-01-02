# Backend Design Specification - Sprint test-2 v1

**Project:** Simple Todo App
**Sprint:** sprint-test-2
**Created By:** @SA
**Date:** 2026-01-01
**Status:** Design Phase

---

## 1. Architecture Overview

### System Architecture

```
┌─────────────┐      HTTPS/REST      ┌─────────────┐
│   React     │ ◄──────────────────► │   Express   │
│   Frontend  │      JSON/JWT        │   Backend   │
└─────────────┘                      └──────┬──────┘
                                            │
                                            │ Prisma ORM
                                            ▼
                                     ┌─────────────┐
                                     │   SQLite    │
                                     │   Database  │
                                     └─────────────┘
```

### Technology Stack
- **Runtime:** Node.js 18+ with TypeScript
- **Framework:** Express.js 4.x
- **Database:** SQLite 3.x
- **ORM:** Prisma 5.x
- **Authentication:** JWT (jsonwebtoken)
- **Validation:** Zod
- **Testing:** Jest + Supertest

### Design Patterns
- **MVC Pattern:** Controllers → Services → Models
- **Repository Pattern:** Data access abstraction via Prisma
- **Middleware Pattern:** Auth, validation, error handling
- **DTO Pattern:** Request/response validation with Zod

---

## 2. Data Models & Schema

### Prisma Schema

```prisma
// prisma/schema.prisma

datasource db {
  provider = "sqlite"
  url      = "file:./dev.db"
}

generator client {
  provider = "prisma-client-js"
}

model User {
  id        String   @id @default(uuid())
  email     String   @unique
  password  String   // bcrypt hashed
  name      String?
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  todos     Todo[]
}

model Todo {
  id          String   @id @default(uuid())
  title       String
  description String?
  status      String   @default("pending") // "pending" | "completed"
  userId      String
  user        User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt

  @@index([userId])
  @@index([status])
}
```

### Entity Relationships
- **User → Todo:** One-to-Many (one user has many todos)
- **Cascade Delete:** Deleting user deletes all their todos

---

## 3. API Specifications

### Base URL
```
Development: http://localhost:3001/api
Production: https://api.todo-app.com/api
```

### Authentication
- **Type:** JWT Bearer Token
- **Header:** `Authorization: Bearer <token>`
- **Token Expiry:** 7 days
- **Refresh:** Not implemented (v1 simplicity)

---

### API Endpoints

#### 3.1 Authentication Endpoints

**POST /api/auth/signup**
```typescript
Request:
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "name": "John Doe"
}

Response: 201 Created
{
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "name": "John Doe"
  },
  "token": "jwt-token-here"
}

Errors:
- 400: Invalid input (email format, password strength)
- 409: Email already exists
```

**POST /api/auth/login**
```typescript
Request:
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}

Response: 200 OK
{
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "name": "John Doe"
  },
  "token": "jwt-token-here"
}

Errors:
- 400: Invalid input
- 401: Invalid credentials
```

**GET /api/auth/me**
```typescript
Headers: Authorization: Bearer <token>

Response: 200 OK
{
  "id": "uuid",
  "email": "user@example.com",
  "name": "John Doe",
  "createdAt": "2026-01-01T00:00:00Z"
}

Errors:
- 401: Unauthorized (no token or invalid token)
```

---

#### 3.2 Todo Endpoints

**GET /api/todos**
```typescript
Headers: Authorization: Bearer <token>
Query Params:
  - status?: "pending" | "completed" | "all" (default: "all")
  - sort?: "createdAt" | "updatedAt" (default: "createdAt")
  - order?: "asc" | "desc" (default: "desc")

Response: 200 OK
{
  "todos": [
    {
      "id": "uuid",
      "title": "Buy groceries",
      "description": "Milk, eggs, bread",
      "status": "pending",
      "createdAt": "2026-01-01T10:00:00Z",
      "updatedAt": "2026-01-01T10:00:00Z"
    }
  ],
  "count": 1
}

Errors:
- 401: Unauthorized
```

**GET /api/todos/:id**
```typescript
Headers: Authorization: Bearer <token>

Response: 200 OK
{
  "id": "uuid",
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "status": "pending",
  "createdAt": "2026-01-01T10:00:00Z",
  "updatedAt": "2026-01-01T10:00:00Z"
}

Errors:
- 401: Unauthorized
- 404: Todo not found
- 403: Forbidden (todo belongs to another user)
```

**POST /api/todos**
```typescript
Headers: Authorization: Bearer <token>
Request:
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread" // optional
}

Response: 201 Created
{
  "id": "uuid",
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "status": "pending",
  "createdAt": "2026-01-01T10:00:00Z",
  "updatedAt": "2026-01-01T10:00:00Z"
}

Errors:
- 400: Invalid input (title required, max length)
- 401: Unauthorized
```

**PATCH /api/todos/:id**
```typescript
Headers: Authorization: Bearer <token>
Request:
{
  "title"?: "Updated title",
  "description"?: "Updated description",
  "status"?: "completed"
}

Response: 200 OK
{
  "id": "uuid",
  "title": "Updated title",
  "description": "Updated description",
  "status": "completed",
  "createdAt": "2026-01-01T10:00:00Z",
  "updatedAt": "2026-01-01T11:00:00Z"
}

Errors:
- 400: Invalid input
- 401: Unauthorized
- 404: Todo not found
- 403: Forbidden
```

**DELETE /api/todos/:id**
```typescript
Headers: Authorization: Bearer <token>

Response: 204 No Content

Errors:
- 401: Unauthorized
- 404: Todo not found
- 403: Forbidden
```

---

## 4. Project Structure

```
backend/
├── src/
│   ├── index.ts                 # App entry point
│   ├── app.ts                   # Express app setup
│   ├── config/
│   │   └── env.ts               # Environment variables
│   ├── middleware/
│   │   ├── auth.ts              # JWT authentication
│   │   ├── errorHandler.ts     # Global error handler
│   │   └── validate.ts          # Request validation
│   ├── routes/
│   │   ├── auth.routes.ts       # Auth endpoints
│   │   └── todo.routes.ts       # Todo endpoints
│   ├── controllers/
│   │   ├── auth.controller.ts   # Auth logic
│   │   └── todo.controller.ts   # Todo logic
│   ├── services/
│   │   ├── auth.service.ts      # Auth business logic
│   │   └── todo.service.ts      # Todo business logic
│   ├── models/
│   │   └── prisma.ts            # Prisma client instance
│   ├── utils/
│   │   ├── jwt.ts               # JWT helpers
│   │   ├── password.ts          # Password hashing
│   │   └── validation.ts        # Zod schemas
│   └── types/
│       └── index.ts             # TypeScript types
├── tests/
│   ├── auth.test.ts
│   └── todo.test.ts
├── prisma/
│   ├── schema.prisma
│   └── migrations/
├── .env
├── .env.example
├── package.json
├── tsconfig.json
└── jest.config.js
```

---

## 5. Error Handling

### Error Response Format
```typescript
{
  "error": {
    "message": "Human-readable error message",
    "code": "ERROR_CODE",
    "details": {} // Optional validation details
  }
}
```

### HTTP Status Codes
- **200:** Success
- **201:** Created
- **204:** No Content
- **400:** Bad Request (validation errors)
- **401:** Unauthorized (missing/invalid token)
- **403:** Forbidden (insufficient permissions)
- **404:** Not Found
- **409:** Conflict (duplicate email)
- **500:** Internal Server Error

### Error Codes
- `VALIDATION_ERROR` - Input validation failed
- `UNAUTHORIZED` - Authentication required
- `FORBIDDEN` - Insufficient permissions
- `NOT_FOUND` - Resource not found
- `DUPLICATE_EMAIL` - Email already registered
- `INVALID_CREDENTIALS` - Wrong email/password
- `INTERNAL_ERROR` - Server error

---

## 6. Security Considerations

### Authentication & Authorization
- ✅ Passwords hashed with bcrypt (10 rounds)
- ✅ JWT tokens signed with HS256
- ✅ Token expiry: 7 days
- ✅ Protected routes require valid JWT
- ✅ User can only access their own todos

### Input Validation
- ✅ All inputs validated with Zod schemas
- ✅ Email format validation
- ✅ Password strength: min 8 chars, uppercase, lowercase, number
- ✅ Title max length: 200 chars
- ✅ Description max length: 1000 chars

### SQL Injection Prevention
- ✅ Prisma ORM (parameterized queries)
- ✅ No raw SQL queries

### CORS Configuration
```typescript
cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:5173',
  credentials: true
})
```

### Rate Limiting
- ⚠️ Not implemented in v1 (could-have feature)

### HTTPS
- ✅ Required in production
- ⚠️ HTTP allowed in development

---

## 7. Performance & Scalability

### Database Optimization
- ✅ Indexes on `userId` and `status` fields
- ✅ Cascade delete for data integrity
- ✅ UUID for distributed systems readiness

### Caching Strategy
- ⚠️ Not implemented in v1 (future enhancement)

### Connection Pooling
- ✅ Prisma handles connection pooling automatically

### Response Time Targets
- Auth endpoints: <100ms
- Todo CRUD: <50ms
- List todos: <100ms

---

## 8. Environment Variables

```bash
# .env.example
NODE_ENV=development
PORT=3001
DATABASE_URL="file:./dev.db"
JWT_SECRET=your-super-secret-jwt-key-change-in-production
JWT_EXPIRY=7d
FRONTEND_URL=http://localhost:5173
```

---

## 9. Testing Strategy

### Unit Tests
- Auth service (signup, login, token generation)
- Todo service (CRUD operations)
- Password hashing utilities
- JWT utilities

### Integration Tests
- API endpoints with Supertest
- Database operations with test database
- Authentication flow
- Authorization checks

### Test Coverage Target
- Minimum: 80%
- Goal: 90%

---

## 10. Deployment Considerations

### Database Migration
```bash
npx prisma migrate deploy
```

### Build Process
```bash
npm run build  # TypeScript → JavaScript
npm start      # Run production server
```

### Health Check Endpoint
```typescript
GET /api/health
Response: 200 OK
{
  "status": "ok",
  "timestamp": "2026-01-01T10:00:00Z"
}
```

---

## Next Step:
- @QA - Please review backend design for testability and completeness
- @SECA - Please check for security vulnerabilities in APIs/data
- @UIUX - Please confirm API endpoints match UI requirements

#designing #backend #architecture #sprint-test-2
