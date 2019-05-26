from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def submit_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("new").click()
        self.fill_group(group=group)
        # Отправляем форму группы
        wd.find_element_by_name("submit").click()
        self.open_group_page()

    def fill_group(self, group):
        filler = self.app.filler
        # Заполняем форму новой группы
        filler.fill_input_field(element="group_name", text=group.name)
        filler.fill_input_field(element="group_header", text=group.header)
        filler.fill_input_field(element="group_footer", text=group.footer)

    def edit_group(self, group):
        wd = self.app.wd
        # Выбираем первую группу
        wd.find_element_by_name("selected[]").click()
        # Жмем на кнопку "редактировать"
        wd.find_element_by_name("edit").click()
        self.fill_group(group=group)
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
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
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

    def get_list(self):
        wd = self.app.wd
        self.open_group_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            group_name = element.text
            group_id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=group_name, group_id=group_id))
        return groups
