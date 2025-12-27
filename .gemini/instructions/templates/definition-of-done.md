# Definition of Done (DoD) Checklist
**Version:** 1.0 | **Last Updated:** 2025-12-23

---

## Purpose
This checklist ensures consistent quality standards across all deliverables. A task is **NOT DONE** until ALL applicable items are checked.

---

## 📋 Development Task DoD

### Code Quality
- [ ] Code implemented according to approved design specs
- [ ] Follows project coding standards and conventions
- [ ] No hardcoded values (use config/environment variables)
- [ ] No console.log / debug code left in production code
- [ ] Proper error handling implemented
- [ ] Code is self-documenting with clear naming

### Testing
- [ ] Unit tests written and passing
- [ ] Local testing passed (all features work as expected)
- [ ] Edge cases handled and tested
- [ ] No regressions introduced

### Documentation
- [ ] Code comments for complex logic
- [ ] API documentation updated (if applicable)
- [ ] Tagged with `#development`

### Evidence
- [ ] Screenshots/recordings captured (if UI changes)
- [ ] Build logs showing success

### Handoff
- [ ] Development-Log artifact updated
- [ ] @TESTER tagged for testing

---

## 🧪 Testing Task DoD

### Test Execution
- [ ] All test cases from Test Plan executed
- [ ] Happy path scenarios verified
- [ ] Error/edge case scenarios verified
- [ ] Acceptance criteria from user stories validated

### Bug Management
- [ ] All bugs logged with proper priority tags
- [ ] No `#fixbug-critical` or `#fixbug-high` bugs remaining open
- [ ] Responsible @DEV tagged for each bug

### Evidence
- [ ] Screenshots/recordings for key flows
- [ ] Screenshots/recordings for each bug found

### Documentation
- [ ] Test-Report artifact created/updated
- [ ] Tagged with `#testing`

### Handoff (if passed)
- [ ] @REPORTER tagged
- [ ] @STAKEHOLDER tagged (if ready for final review)

---

## 🚀 Deployment Task DoD

### Pre-Deployment
- [ ] All tests passing in CI/CD pipeline
- [ ] Security checklist completed
- [ ] Environment variables configured correctly
- [ ] Database migrations ready (if applicable)

### Staging
- [ ] Deployed to staging environment successfully
- [ ] Smoke tests passed on staging
- [ ] Tagged with `#deployed-staging`

### Production
- [ ] Staging approved by @TESTER
- [ ] Deployed to production environment
- [ ] Health checks passing
- [ ] Monitoring/alerting configured
- [ ] Tagged with `#deployed-production`

### Documentation
- [ ] DevOps-Plan-and-Log artifact updated
- [ ] Deployment steps documented

### Rollback
- [ ] Rollback plan documented and tested

---

## 📊 Design Task DoD

### Design Quality
- [ ] All Must-Have requirements addressed
- [ ] Consistent with project plan scope
- [ ] Diagrams/mockups are clear and complete
- [ ] APIs designed for both UI needs and backend feasibility

### Review Readiness
- [ ] Design-Spec artifact created with proper naming
- [ ] Tagged with `#designing` or `#uiux-design`

### Handoff
- [ ] @QA tagged for design verification
- [ ] @SECA tagged for security review

---

## ✅ Project Completion DoD

### Feature Delivery
- [ ] All Must-Have features implemented and verified
- [ ] All Should-Have features implemented (or justified deferral)
- [ ] No `#fixbug-critical` or `#fixbug-high` bugs remaining

### Approvals
- [ ] Design approved by QA + SecA
- [ ] Testing passed by TESTER
- [ ] STAKEHOLDER final approval received

### Documentation
- [ ] Master-Documentation.md complete and current
- [ ] Final-Project-Report.md created by REPORTER
- [ ] All artifacts versioned and archived

### Notification
- [ ] User notified of project completion
- [ ] Handover documentation provided (if applicable)

---

## Quick Reference Card

| Task Type | Key Criteria | Tags |
|-----------|--------------|------|
| **Development** | Code works, tests pass, evidence captured | `#development` |
| **Testing** | All cases run, no critical/high bugs | `#testing` |
| **Deployment** | CI passes, staging verified, rollback ready | `#deployed-*` |
| **Design** | Covers requirements, diagrams clear | `#designing` |
| **Project** | All features done, stakeholder approved | `#reporting` |

---

#global-rules #definition-of-done
