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
        wd.find_element_by_link_text("group page").click()


    def create(self, group):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")
        self.submit_group(group)

