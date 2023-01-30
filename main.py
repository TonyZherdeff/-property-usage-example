class Money:
    def __init__(self, name, m_num, s_num, icon):
        self.name = name
        self.m_num = m_num
        self.s_num = s_num
        self.icon = icon

    @property
    def print_class(self):
        return f'{self.name} {self.m_num}.{self.s_num} {self.icon}'


bucks = Money("USD", 20, 45, chr(36))
print(bucks.print_class)