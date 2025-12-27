# Backend Design Specification - Version [X]

## Document Info
| Field | Value |
|-------|-------|
| Version | [X.0] |
| Date | [YYYY-MM-DD] |
| Author | @SA |
| Status | Draft / Review / Approved |

---

## 1. Architecture Overview

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│   API       │────▶│  Database   │
│  (Browser)  │     │   Layer     │     │             │
└─────────────┘     └─────────────┘     └─────────────┘
```

## 2. Technology Stack
| Layer | Technology | Justification |
|-------|------------|---------------|
| Runtime | [e.g., Node.js 20] | [Reason] |
| Framework | [e.g., SvelteKit] | [Reason] |
| Database | [e.g., PostgreSQL] | [Reason] |
| Auth | [e.g., Supabase Auth] | [Reason] |

## 3. API Endpoints

### 3.1 [Resource Name]
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | /api/[resource] | List all | Required |
| POST | /api/[resource] | Create new | Required |
| PUT | /api/[resource]/:id | Update | Required |
| DELETE | /api/[resource]/:id | Delete | Required |

**Request/Response Example:**
```json
// POST /api/[resource]
// Request
{ "field": "value" }

// Response 201
{ "id": "uuid", "field": "value", "createdAt": "ISO8601" }
```

## 4. Database Schema

### 4.1 [Table Name]
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PK, NOT NULL | Primary key |
| created_at | TIMESTAMP | NOT NULL | Creation time |
| [field] | [TYPE] | [Constraints] | [Description] |

### 4.2 Relationships
```
[Table A] 1──────N [Table B]
              └── foreign_key: table_a_id
```

## 5. Authentication & Authorization
| Role | Permissions |
|------|-------------|
| Guest | Read public |
| User | Read/Write own |
| Admin | Full access |

## 6. Error Handling
| Code | Meaning | Response |
|------|---------|----------|
| 400 | Bad Request | { "error": "message" } |
| 401 | Unauthorized | { "error": "Not authenticated" } |
| 403 | Forbidden | { "error": "Access denied" } |
| 404 | Not Found | { "error": "Resource not found" } |
| 500 | Server Error | { "error": "Internal error" } |

## 7. Open Questions
- [ ] @UIUX: [Question about UI requirements]
- [ ] @PO: [Question about business logic]

---

### Next Step:
- @QA - Review design for testability
- @SECA - Security review of API and auth design
- @DEV - Prepare for implementation

#designing
