from model.group import Group


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
        self.create_if_none()
        self.edit_group(group)

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        self.create_if_none()
        # Отмечаем первую группу
        wd.find_element_by_name("selected[]").click()
        # Удаляем отмеченную группу
        wd.find_element_by_name("delete").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create_if_none(self):
        if self.count() == 0:
            self.submit_group(Group(name="test", header="test", footer="test"))
