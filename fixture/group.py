class GroupHelper:
    def __init__(self, app):
        self.app = app

    def submit_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("new").click()
        # Заполняем форму новой группы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Отправляем форму группы
        wd.find_element_by_name("submit").click()
        self.open_group_page()

    def edit_group(self, group):
        wd = self.app.wd
        # Выбираем первую группу
        wd.find_element_by_name("selected[]").click()
        # Жмем на кнопку "редактировать"
        wd.find_element_by_name("edit").click()
        # Заполняем форму новой группы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Отправляем форму группы
        wd.find_element_by_name("update").click()
        self.open_group_page()

    def create(self, group):
        self.open_group_page()
        self.submit_group(group)

    def edit_first(self, group):
        self.open_group_page()
        self.edit_group(group)

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        # Отмечаем первую группу
        wd.find_element_by_name("selected[]").click()
        # Удаляем отмеченную группу
        wd.find_element_by_name("delete").click()
