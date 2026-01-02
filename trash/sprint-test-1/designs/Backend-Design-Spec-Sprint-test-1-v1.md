# Backend Design Specification - Sprint test-1 - v1

**Project:** Simple Todo App (Workflow System Test)
**Sprint:** test-1
**Version:** 1
**Date:** 2026-01-01
**SA:** @SA
**Status:** Ready for Review

---

## 1. Architecture Overview

### 1.1 System Architecture

```
┌─────────────────┐
│   React Client  │
│   (Frontend)    │
└────────┬────────┘
         │ HTTP/REST
         ↓
┌─────────────────┐
│  Express Server │
│   (Backend)     │
└────────┬────────┘
         │ Mongoose
         ↓
┌─────────────────┐
│    MongoDB      │
│   (Database)    │
└─────────────────┘
```

### 1.2 Technology Stack

**Backend:**
- Node.js 18+
- Express.js 4.x
- Mongoose 7.x
- CORS middleware
- Body-parser

**Database:**
- MongoDB 6.x
- Collections: tasks

---

## 2. Data Models

### 2.1 Task Model

```javascript
const TaskSchema = new Schema({
  title: {
    type: String,
    required: true,
    trim: true,
    maxlength: 200
  },
  description: {
    type: String,
    trim: true,
    maxlength: 1000
  },
  priority: {
    type: String,
    enum: ['high', 'medium', 'low'],
    default: 'medium'
  },
  status: {
    type: String,
    enum: ['todo', 'in-progress', 'done'],
    default: 'todo'
  },
  createdAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
});
```

### 2.2 Database Schema

**Collection: tasks**
```
{
  _id: ObjectId,
  title: String (required, max 200),
  description: String (optional, max 1000),
  priority: String (enum: high|medium|low),
  status: String (enum: todo|in-progress|done),
  createdAt: Date,
  updatedAt: Date
}
```

---

## 3. API Specifications

### 3.1 Base URL
```
http://localhost:3000/api
```

### 3.2 Endpoints

#### GET /tasks
**Description:** Get all tasks

**Query Parameters:**
- `status` (optional): Filter by status (todo|in-progress|done)
- `priority` (optional): Filter by priority (high|medium|low)

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "_id": "507f1f77bcf86cd799439011",
      "title": "Complete project",
      "description": "Finish the todo app",
      "priority": "high",
      "status": "in-progress",
      "createdAt": "2026-01-01T10:00:00Z",
      "updatedAt": "2026-01-01T10:00:00Z"
    }
  ]
}
```

---

#### GET /tasks/:id
**Description:** Get single task by ID

**Response:**
```json
{
  "success": true,
  "data": {
    "_id": "507f1f77bcf86cd799439011",
    "title": "Complete project",
    "description": "Finish the todo app",
    "priority": "high",
    "status": "in-progress",
    "createdAt": "2026-01-01T10:00:00Z",
    "updatedAt": "2026-01-01T10:00:00Z"
  }
}
```

---

#### POST /tasks
**Description:** Create new task

**Request Body:**
```json
{
  "title": "New task",
  "description": "Task description",
  "priority": "medium",
  "status": "todo"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "_id": "507f1f77bcf86cd799439011",
    "title": "New task",
    "description": "Task description",
    "priority": "medium",
    "status": "todo",
    "createdAt": "2026-01-01T10:00:00Z",
    "updatedAt": "2026-01-01T10:00:00Z"
  }
}
```

---

#### PUT /tasks/:id
**Description:** Update existing task

**Request Body:**
```json
{
  "title": "Updated task",
  "description": "Updated description",
  "priority": "high",
  "status": "in-progress"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "_id": "507f1f77bcf86cd799439011",
    "title": "Updated task",
    "description": "Updated description",
    "priority": "high",
    "status": "in-progress",
    "createdAt": "2026-01-01T10:00:00Z",
    "updatedAt": "2026-01-01T11:00:00Z"
  }
}
```

---

#### DELETE /tasks/:id
**Description:** Delete task

**Response:**
```json
{
  "success": true,
  "message": "Task deleted successfully"
}
```

---

### 3.3 Error Responses

**400 Bad Request:**
```json
{
  "success": false,
  "error": "Validation error",
  "details": "Title is required"
}
```

**404 Not Found:**
```json
{
  "success": false,
  "error": "Task not found"
}
```

**500 Internal Server Error:**
```json
{
  "success": false,
  "error": "Internal server error",
  "message": "Database connection failed"
}
```

---

## 4. Integration Points

### 4.1 Frontend Integration
- React app makes HTTP requests to Express API
- CORS enabled for localhost:3001
- JSON data format
- RESTful conventions

### 4.2 Database Integration
- Mongoose ODM for MongoDB
- Connection string: `mongodb://localhost:27017/todoapp`
- Auto-reconnect enabled
- Connection pooling

---

## 5. Error Handling

### 5.1 Validation Errors
- Check required fields
- Validate enum values
- Validate string lengths
- Return 400 status with details

### 5.2 Database Errors
- Handle connection failures
- Handle query errors
- Return 500 status with message
- Log errors for debugging

### 5.3 Not Found Errors
- Check if resource exists
- Return 404 status
- Clear error message

---

## 6. Security Considerations

### 6.1 Input Validation
- Sanitize user input
- Validate data types
- Check string lengths
- Prevent injection attacks

### 6.2 CORS Configuration
- Allow specific origins only
- Restrict methods (GET, POST, PUT, DELETE)
- No credentials in test environment

### 6.3 Error Messages
- Don't expose internal details
- Generic error messages for users
- Detailed logs for developers

---

## 7. Performance & Scalability

### 7.1 Database Indexing
```javascript
TaskSchema.index({ status: 1 });
TaskSchema.index({ priority: 1 });
TaskSchema.index({ createdAt: -1 });
```

### 7.2 Query Optimization
- Use lean() for read-only queries
- Limit result sets
- Use projection to select fields

### 7.3 Caching Strategy
- Not required for test app
- Can add Redis later if needed

---

## 8. Next Steps

### After Design Approval:
- @QA - Please review backend design for testability and completeness
- @SECA - Please check for security vulnerabilities in APIs/data
- @UIUX - Please confirm API endpoints match UI requirements

#designing #backend #architecture #workflow-test #sprint-test-1
