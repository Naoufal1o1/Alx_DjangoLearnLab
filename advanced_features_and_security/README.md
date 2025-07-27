# Permissions & Groups – Alx_DjangoLearnLab

## Permissions Defined in Article Model
- can_view
- can_create
- can_edit
- can_delete

## User Groups & Their Permissions

| Group   | Permissions                        |
|---------|------------------------------------|
| Admins  | can_view, can_create, can_edit, can_delete |
| Editors | can_create, can_edit               |
| Viewers | can_view                           |

## Enforced in Views
Each view uses `@permission_required` decorator to restrict access based on role.

Example:
```python
@permission_required('advanced_features_and_security.can_edit', raise_exception=True)


---

Would you like me to generate the template HTML files (`list.html`, `form.html`, `confirm_delete.html`) or a Django shell script to bulk-create groups and permissions?
