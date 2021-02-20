class Formatter:
    def __init__(self):
        self.number_pages = True
        self.generate_title_page = False
        self.primary_title_text = None
        self.secondary_title_text = None
        self.duration = None
        self.examiner = None
        self.date = None
        self.mark_total = None
        self.left_header = None
        self.right_header = None
        self.left_footer = None
        self.right_footer = None

        # regarding page num as a flag in the header/footer, revisit this

    def has_numbebered_pages(self, show_page_num=False):
        if(type(show_page_num) != bool):
            raise TypeError('show page num was not bool')
        self.number_pages = show_page_num
        print('setting number pages flag to '+ str(show_page_num))
        
    def has_title_page(self, show_title_page=False):
        if(type(show_title_page) != bool):
            raise TypeError('show title page was not bool')
        self.generate_title_page = show_title_page
        print('setting titles pages flag to '+ str(show_title_page))
        
    def set_primary_title_text(self, text):
        if(type(text) != str):
            raise TypeError('primary title text was not string')
        self.primary_title_text = text
        print('setting primary title to '+ text)
        
    def set_secondary_title_text(self, text):
        if(type(text) != str):
            raise TypeError('secondary title text was not string')
        self.secondary_title_text = text
        print('setting secondary title to '+ text)
        
    def set_duration(self, text):
        if(type(text) != str):
            raise TypeError('duration value was not string')
        self.duration = text
        print('setting duration to '+ text)
        
    def set_examiner(self, text):
        if(type(text) != str):
            raise TypeError('examiner value was not string')
        self.examiner = text
        print('setting examiner to '+ text)
        
    def set_date(self, text):
        if(type(text) != str):
            raise TypeError('date value was not string')
        self.date = text
        print('setting date to '+ text)
        
    def set_mark_total(self, total_marks):
        if(type(total_marks) != int):
            raise TypeError('total marks value was not int')
        self.mark_total = total_marks
        print('setting marks to '+ str(total_marks))
        
    def set_left_header(self, text):
        if(type(text) != str):
            raise TypeError('left header was not string')
        self.left_header = text
        print('setting left header to '+ text)
        
    def set_right_header(self, text):
        if(type(text) != str):
            raise TypeError('right header was not string')
        self.right_header = text
        
    def set_left_footer(self, text):
        if(type(text) != str):
            raise TypeError('left footer was not string')
        self.left_footer = text
        
    def set_right_footer(self, text):
        if(type(text) != str):
            raise TypeError('right footer was not string')
        self.right_footer = text
        print('setting footer right to '+ text)