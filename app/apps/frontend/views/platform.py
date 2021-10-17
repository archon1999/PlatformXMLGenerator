from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from apps.backend.models import Platform, Project


class PlatformView(View):
    template_name = 'platform/index.html'

    def get(self, request, platform_id):
        user = request.user
        platform = get_object_or_404(Platform, id=platform_id)
        projects = platform.projects.filter(user=user).order_by('uid')
        return render(request, self.template_name, {
            'platform': platform,
            'projects': projects,
        })


class NewProjectView(View):
    def post(self, request, platform_id):
        user = request.user
        if (project_name := request.POST.get('project_name')):
            platform = Platform.platforms.get(id=platform_id)
            Project.projects.create(
                name=project_name,
                platform=platform,
                user=user,
            )

        return redirect('platform', platform_id=platform_id)


class EditProjectView(View):
    def post(self, request, platform_id, project_id):
        if (project_name := request.POST.get('project_name', None)):
            project = Project.projects.get(id=project_id)
            user = request.user
            if user == project.user:
                project.name = project_name
                project.save()

        return redirect('platform', platform_id=platform_id)


class DeleteProjectView(View):
    def get(self, request, platform_id, project_id):
        project = Project.projects.get(id=project_id)
        user = request.user
        if user == project.user:
            project.delete()

        return redirect('platform', platform_id=platform_id)


class ProjectsReOrderView(View):
    def post(self, request, platform_id):
        platform = Platform.platforms.get(id=platform_id)
        user = request.user
        id_list = request.POST.getlist('id_list[]', [])
        for index, id in enumerate(id_list):
            project = Project.projects.get(
                user=user,
                platform=platform,
                id=id,
            )
            project.uid = index
            project.save()

        return redirect('platform', platform_id=platform_id)
