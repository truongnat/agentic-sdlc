# Product Backlog - Sprint test-2 v1

**Project:** Simple Todo App
**Sprint:** sprint-test-2
**Created By:** @PO
**Date:** 2026-01-01
**Status:** Design Phase

---

## Backlog Overview

**Total Features:** 12
- **Must-Have (P0):** 8 features
- **Should-Have (P1):** 3 features
- **Could-Have (P2):** 1 feature

**Estimated Effort:** 11.5 hours
**Business Value:** High (validates complete workflow)

---

## Must-Have Features (P0)

### F1: User Registration
**Priority:** P0 - Must Have
**User Story:** As a new user, I want to create an account so that I can save my todos securely.

**Acceptance Criteria:**
- ✅ User can sign up with email, password, and name
- ✅ Email must be unique
- ✅ Password must be at least 8 characters with uppercase, lowercase, and number
- ✅ User receives JWT token upon successful signup
- ✅ User is automatically logged in after signup

**Technical Tasks:**
- Backend: POST /api/auth/signup endpoint
- Frontend: Signup form component
- Validation: Email format, password strength
- Database: User model with bcrypt password hashing

**Estimated Effort:** 1.5 hours

---

### F2: User Login
**Priority:** P0 - Must Have
**User Story:** As a returning user, I want to log in so that I can access my todos.

**Acceptance Criteria:**
- ✅ User can login with email and password
- ✅ Invalid credentials show error message
- ✅ Successful login returns JWT token
- ✅ Token is stored securely (localStorage/sessionStorage)
- ✅ User is redirected to todo list after login

**Technical Tasks:**
- Backend: POST /api/auth/login endpoint
- Frontend: Login form component
- Auth: JWT token generation and validation
- Error handling: Invalid credentials

**Estimated Effort:** 1 hour

---

### F3: User Logout
**Priority:** P0 - Must Have
**User Story:** As a logged-in user, I want to log out so that my account is secure.

**Acceptance Criteria:**
- ✅ User can click logout button
- ✅ Token is removed from storage
- ✅ User is redirected to login page
- ✅ Protected routes are inaccessible after logout

**Technical Tasks:**
- Frontend: Logout button and handler
- Auth: Clear token from storage
- Routing: Redirect to login

**Estimated Effort:** 0.5 hours

---

### F4: Create Todo
**Priority:** P0 - Must Have
**User Story:** As a user, I want to create a new todo so that I can track my tasks.

**Acceptance Criteria:**
- ✅ User can click "Add Todo" button
- ✅ Modal/form opens with title and description fields
- ✅ Title is required, description is optional
- ✅ Todo is saved to database with user association
- ✅ New todo appears in list immediately
- ✅ Success message is shown

**Technical Tasks:**
- Backend: POST /api/todos endpoint
- Frontend: Add todo modal/form component
- Validation: Title required, max lengths
- UI: Success feedback

**Estimated Effort:** 1.5 hours

---

### F5: View Todo List
**Priority:** P0 - Must Have
**User Story:** As a user, I want to see all my todos so that I know what I need to do.

**Acceptance Criteria:**
- ✅ User sees list of all their todos on main page
- ✅ Each todo shows title, description, status, date
- ✅ Todos are sorted by creation date (newest first)
- ✅ Empty state shown when no todos exist
- ✅ Only user's own todos are visible

**Technical Tasks:**
- Backend: GET /api/todos endpoint with filtering
- Frontend: Todo list component
- UI: Todo item card component
- Empty state: Friendly message

**Estimated Effort:** 1.5 hours

---

### F6: Update Todo
**Priority:** P0 - Must Have
**User Story:** As a user, I want to edit my todos so that I can update task details.

**Acceptance Criteria:**
- ✅ User can click edit icon on todo
- ✅ Modal opens with pre-filled data
- ✅ User can modify title, description, status
- ✅ Changes are saved to database
- ✅ Updated todo reflects changes immediately
- ✅ Success message is shown

**Technical Tasks:**
- Backend: PATCH /api/todos/:id endpoint
- Frontend: Edit todo modal component
- State management: Update local state
- Validation: Same as create

**Estimated Effort:** 1.5 hours

---

### F7: Delete Todo
**Priority:** P0 - Must Have
**User Story:** As a user, I want to delete todos so that I can remove completed or unwanted tasks.

**Acceptance Criteria:**
- ✅ User can click delete icon on todo
- ✅ Confirmation dialog appears
- ✅ Todo is removed from database
- ✅ Todo disappears from list immediately
- ✅ Success message is shown

**Technical Tasks:**
- Backend: DELETE /api/todos/:id endpoint
- Frontend: Delete confirmation dialog
- State management: Remove from local state
- UI: Smooth removal animation

**Estimated Effort:** 1 hour

---

### F8: Toggle Todo Status
**Priority:** P0 - Must Have
**User Story:** As a user, I want to mark todos as complete so that I can track my progress.

**Acceptance Criteria:**
- ✅ User can click checkbox to toggle status
- ✅ Status updates immediately (pending ↔ completed)
- ✅ Completed todos show visual difference (strikethrough, opacity)
- ✅ Change is saved to database
- ✅ No page reload required

**Technical Tasks:**
- Backend: PATCH /api/todos/:id (status field)
- Frontend: Checkbox component with handler
- UI: Visual feedback for completed state
- Optimistic updates

**Estimated Effort:** 1 hour

---

## Should-Have Features (P1)

### F9: Filter Todos by Status
**Priority:** P1 - Should Have
**User Story:** As a user, I want to filter todos by status so that I can focus on pending or completed tasks.

**Acceptance Criteria:**
- ✅ Filter dropdown with options: All, Pending, Completed
- ✅ Selecting filter updates todo list
- ✅ Filter state persists during session
- ✅ URL reflects current filter (optional)

**Technical Tasks:**
- Backend: Query parameter support in GET /api/todos
- Frontend: Filter dropdown component
- State management: Filter state
- URL: Query params (optional)

**Estimated Effort:** 1 hour

---

### F10: Responsive Design
**Priority:** P1 - Should Have
**User Story:** As a mobile user, I want the app to work on my phone so that I can manage todos on-the-go.

**Acceptance Criteria:**
- ✅ App works on mobile (< 640px)
- ✅ App works on tablet (640px - 1024px)
- ✅ App works on desktop (> 1024px)
- ✅ Touch targets are at least 44x44px
- ✅ No horizontal scrolling

**Technical Tasks:**
- Frontend: Responsive CSS with Tailwind
- Testing: Test on multiple screen sizes
- UI: Mobile-optimized modals (bottom sheets)

**Estimated Effort:** 1 hour

---

### F11: Data Persistence
**Priority:** P1 - Should Have
**User Story:** As a user, I want my todos to be saved so that they don't disappear when I refresh the page.

**Acceptance Criteria:**
- ✅ Todos are stored in SQLite database
- ✅ Data survives server restart
- ✅ User authentication persists (JWT in storage)
- ✅ No data loss on page refresh

**Technical Tasks:**
- Backend: Prisma + SQLite setup
- Database: Migrations and schema
- Frontend: Token storage in localStorage
- Testing: Verify persistence

**Estimated Effort:** 0.5 hours (included in backend setup)

---

## Could-Have Features (P2)

### F12: Sort Todos
**Priority:** P2 - Could Have
**User Story:** As a user, I want to sort todos by date so that I can see newest or oldest first.

**Acceptance Criteria:**
- ✅ Sort dropdown with options: Newest, Oldest
- ✅ Selecting sort updates todo list order
- ✅ Sort state persists during session

**Technical Tasks:**
- Backend: Sort parameter in GET /api/todos
- Frontend: Sort dropdown component
- State management: Sort state

**Estimated Effort:** 0.5 hours

---

## User Stories Summary

### Epic 1: Authentication (3 stories)
- F1: User Registration
- F2: User Login
- F3: User Logout

### Epic 2: Todo Management (5 stories)
- F4: Create Todo
- F5: View Todo List
- F6: Update Todo
- F7: Delete Todo
- F8: Toggle Todo Status

### Epic 3: User Experience (4 stories)
- F9: Filter Todos
- F10: Responsive Design
- F11: Data Persistence
- F12: Sort Todos

---

## Priority Rationale

### Why P0 (Must-Have)?
- Core CRUD functionality required for MVP
- Authentication essential for multi-user app
- Without these, app has no value

### Why P1 (Should-Have)?
- Significantly improves user experience
- Expected by modern users
- Relatively low effort, high impact

### Why P2 (Could-Have)?
- Nice-to-have enhancements
- Can be added in future iterations
- Not critical for initial launch

---

## Acceptance Criteria Alignment

All features align with project plan success criteria:
- ✅ All CRUD operations working (F4-F8)
- ✅ User authentication implemented (F1-F3)
- ✅ Responsive UI across devices (F10)
- ✅ Data persistence (F11)

---

## Next Step:
- @PM - Backlog aligned with project plan
- @SA @UIUX - Top priority features ready for design review
- @QA - Ready for design verification
- @SECA - Ready for security review

#product-owner #backlog #sprint-test-2
