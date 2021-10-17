from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from apps.backend.models import Project


def calc_level(category):
    if category.parent is None:
        category.level = 1
    else:
        if not hasattr(category.parent, 'level'):
            calc_level(category.parent)

        category.level = category.parent.level + 1


class ProjectView(View):
    template_name = 'platform/project.html'

    def get(self, request, platform_id, project_id):
        user = request.user
        project = get_object_or_404(Project, id=project_id)
        if project.user != user:
            return redirect('/')

        platform = project.platform
        projects = platform.projects.filter(user=user).order_by('uid')
        categories = platform.categories.all()
        for category in categories:
            calc_level(category)

        return render(request, self.template_name, {
            'platform': platform,
            'project': project,
            'projects': projects,
            'categories': categories,
        })


class ProjectNewCategoryView(View):
    def post(self, request, platform_id, project_id):
        user = request.user
        project = get_object_or_404(Project, id=project_id)
        if user != project.user:
            return redirect('/')

        if (category_id := request.POST.get('category_id', None)):
            project.categories.get_or_create(
                category_id=category_id,
            )

        return redirect('project',
                        platform_id=platform_id, project_id=project_id)


class ProjectDeleteCategoryView(View):
    def post(self, request, platform_id, project_id):
        user = request.user
        project = get_object_or_404(Project, id=project_id)
        if user != project.user:
            return redirect('/')

        for key, value in request.POST.items():
            if key.startswith('checkbox-') and value == 'on':
                category_id = key.removeprefix('checkbox-')
                project.categories.get(id=category_id).delete()

        return redirect('project',
                        platform_id=platform_id, project_id=project_id)
