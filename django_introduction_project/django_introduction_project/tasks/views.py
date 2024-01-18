from django.shortcuts import render

from django_introduction_project.tasks.models import Task


# FBV
# def index(request):
# 	content = "<h1>It works!</h1>" + \
# 		"<p>You are in my project !</p>" + \
# 		"<ul><li>1</li><li>2</li></ul>"
#
# 	return http.HttpResponse(content)

# def index(request):
# 	title_filter = request.GET.get("filter", None)
#
# 	tasks = Task.objects.all()
#
# 	if title_filter:
# 		tasks = tasks.filter(title__contains=title_filter.lower())
#
# 	if not tasks:
# 		return HttpResponse("<h1>No tasks !!!</h1>")
#
# 	result = []
#
# 	for task in tasks:
# 		result.append(F"""
# 	<li>
# 		<h2>{task.title}</h2>
# 		<p>{task.description}</p>
# 	</li>
# 		""")
#
# 		ul = f"<ul>{''.join(result)}</ul>"
#
# 		content = f"""
# 		<h1>{len(tasks)} Tasks</h1>
# 		{ul}
# 		"""
# 	# return HttpResponse(content)

def index(request):
	title_filter = request.GET.get("title_filter", "")

	tasks = Task.objects.all()

	if title_filter:
		tasks = tasks.filter(title__icontains=title_filter.lower())

	context = {
		"title": "The tasks app !!!",
		"task_list": tasks,
		"tasks_list_count": tasks.count(),
		"title_filter": title_filter,
	}
	return render(
		request,
		"tasks/index.html",
		context,
	)
