main_menu = [
    {'title': 'Клубы', 'url': 'collab:all_clubs', 'menu_slug': 'all_clubs'},
    {'title': 'Профиль пользователя', 'url': 'collab:profile_user', 'menu_slug': 'profile_user'},
    {'title': 'Создать клуб', 'url': 'collab:create_club', 'menu_slug': 'create_club'},
    {'title': 'Войти', 'url': 'users:login', 'menu_slug': 'login'},
    {'title': 'Админка', 'url': 'admin:index', 'menu_slug': 'admin'},
]



def menu(request):
    return {'menu': main_menu}