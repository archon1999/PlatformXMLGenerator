from django import template


register = template.Library()


@register.filter
def get_path_items(path):
    items = ['Главная страица'] + path.strip('/').split('/')
    filtered_items = []
    for item in items:
        if not item.isdigit() and item:
            filtered_item = item.replace('-', ' ')
            if filtered_item.find('_') == -1:
                filtered_item = filtered_item.capitalize()

            filtered_items.append(filtered_item)

    return filtered_items
