from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app
        self.group_cache = None

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

    def edit_group_by_index(self, group, index):
        wd = self.app.wd
        self.select_by_index(index)
        # Жмем на кнопку "редактировать"
        wd.find_element_by_name("edit").click()
        self.fill_group(group=group)
        # Отправляем форму группы
        wd.find_element_by_name("update").click()
        self.open_group_page()

    def create(self, group):
        self.open_group_page()
        self.submit_group(group)
        self.group_cache = None

    def edit_first(self, group):
        self.open_group_page()
        self.edit_group_by_index(group=group, index=0)
        self.group_cache = None

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_by_index(index)
        # Удаляем отмеченную группу
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create_if_none(self):
        if self.count() == 0:
            self.submit_group(Group(name="test", header="test", footer="test"))
            self.group_cache = None

    def get_list(self):
        group_cache = self.group_cache
        if group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                group_name = element.text
                group_id = element.find_element_by_name("selected[]").get_attribute("value")
                group_cache.append(Group(name=group_name, group_id=group_id))
        return list(group_cache)
