from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Criar o grupo Creator
creator_group, created = Group.objects.get_or_create(name="Creator")
if not created:
    print("Error creating Creator group")
else:
    print("Created Creator group successfully")

# Criar o grupo Reviewer
reviewer_group, created = Group.objects.get_or_create(name="Reviewer")
if not created:
    print("Error creating Reviewer group")
else:
    print("Created Reviewer group successfully")

# Criar o grupo Solver
solver_group, created = Group.objects.get_or_create(name="Solver")
if not created:
    print("Error creating Solver group")
else:
    print("Created Solver group successfully")

# Criar permissões
kahucuser_model = get_user_model()
content_type = ContentType.objects.get_for_model(kahucuser_model)
can_create_quiz_permission = Permission.objects.create(codename='can_create_quiz',
                                                       name='Can create quiz',
                                                       content_type=content_type)
can_review_quiz_permission = Permission.objects.create(codename='can_review_quiz',
                                                       name='Can review quiz',
                                                       content_type=content_type)
can_create_test_permission = Permission.objects.create(codename='can_create_test',
                                                       name='Can create test',
                                                       content_type=content_type)
can_solve_test_permission = Permission.objects.create(codename='can_solve_test',
                                                      name='Can solve test',
                                                      content_type=content_type)

# Adicionar permissões aos grupos
creator_group.permissions.add(can_create_quiz_permission)
reviewer_group.permissions.add(can_create_quiz_permission, can_review_quiz_permission)
solver_group.permissions.add(can_create_quiz_permission, can_review_quiz_permission, can_solve_test_permission)


