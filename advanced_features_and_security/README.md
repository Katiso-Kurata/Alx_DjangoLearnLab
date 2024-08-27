installation

# Permissions and Groups in relationship_app

## Custom Permissions

In the `Article` model, the following custom permissions have been defined:

- `can_view`: Allows viewing articles.
- `can_create`: Allows creating new articles.
- `can_edit`: Allows editing existing articles.
- `can_delete`: Allows deleting articles.

## Groups

The following groups are configured:

- **Editors**: Can view, create, and edit articles.
- **Viewers**: Can only view articles.
- **Admins**: Can perform all actions.

## Enforcing Permissions in Views

Permissions are enforced in views using Django's `@permission_required` decorator.

- `view_article`: Requires `can_view` permission.
- `create_article`: Requires `can_create` permission.
- `edit_article`: Requires `can_edit` permission.
- `delete_article`: Requires `can_delete` permission.

Make sure to assign users to the appropriate groups to manage access effectively.
