import os


class Student:
    #构造方法,创建对象时自动调用(148)
    def __init__(self, no, name, chinese, math, english):
        self.no = no   #学号
        self.name = name  #姓名
        self.chinese = int(chinese) #语文
        self.math = int(math) #数学
        self.english = int(english)  #英语


class StudentList:
    def __init__(self):
        self.stulist = []   #学生信息

    def show(self):
        # 显示学生信息
        print('{:8}\t{:8}\t{:8}\t{:8}\t{:8}'
              .format('学号', '姓名', '语文', '数学', '英语'))
        for stu in self.stulist:
            print('{:8}\t{:8}\t{:<8}\t{:<8}\t{:<8}'
                  .format(stu.no, stu.name, stu.chinese, stu.math, stu.english))

    def __enterScore(self, message):
        # 成绩输入
        while True:
            try:
                score = input(message)
                if 0 <= int(score) <= 100:
                    break
                else:
                    print("输入错误，成绩应在0到100之间")
            except:
                print("输入错误，成绩应在0到100之间")
        return score

    def __exists(self, no):  #调用这个函数就会返回True,或者False
        # 判断学号是否存在
        for stu in self.stulist:
            if stu.no == no:
                return True
        else:
            return False

    def insert(self):
        # 添加学生信息
        while True:
            no = input('学号:')
            # 如果函数里返回的是True,打印该学号已存在
            if self.__exists(no):
                print('该学号已存在')
            else:
                name = input('姓名:')
                chinese = self.__enterScore('语文成绩:')
                math = self.__enterScore('数学成绩:')
                english = self.__enterScore('英语成绩:')
                stu = Student(no, name, chinese, math, english)
                self.stulist.append(stu)
                # lower是将所有的大写字母转换为小写字母
            choice = input('继续添加(y/n)?').lower()
            if choice == 'n':
                break

    def delete(self):
        # 删除学生信息
        while True:
            no = input('请输入要删除的学生学号:')
            for stu in self.stulist[::]:
                if stu.no == no:
                    # 删除这个学生的所有信息
                    self.stulist.remove(stu)
                    print('删除成功')
                    break
            else:
                print('该学号不存在')
            choice = input('继续删除(y/n)?').lower()
            if choice == 'n':
                break

    def update(self):
        # 修改学生信息
        while True:
            no = input('请输入要修改的学生学号:')
            if self.__exists(no):
                for stu in self.stulist:
                    if stu.no == no:
                        # 把这些信息添加到stulist这个列表中
                        stu.name = input('姓名:')
                        stu.chinese = int(self.__enterScore('语文成绩:'))
                        stu.math = int(self.__enterScore('数学成绩:'))
                        stu.english = int(self.__enterScore('英语成绩:'))
                        print('修改成功')
                        break
            else:
                print('该学号不存在')
            choice = input('继续修改(y/n)?').lower()
            if choice == 'n':
                break

    def load(self, fn):
        # 导入学生信息
        if os.path.exists(fn):
            try:
                with open(fn, 'r', encoding='utf-8') as fp:
                    while True:
                        fs = fp.readline().strip('\n')
                        if not fs:
                            break
                        else:
                            stu = Student(*fs.split(','))
                            if self.__exists(stu.no):
                                print('该学号已存在')
                            else:
                                self.stulist.append(stu)
                print('导入完毕')
            except:
                print('error...')  # 要导入的文件不是utf-8编码，或是字段数不匹配等
        else:
            print('要导入的文件不存在')

    def save(self, fn):
        # 导出学生信息
        with open(fn, 'w', encoding='utf-8') as fp:
            for stu in self.stulist:
                fp.write(stu.no + ',')
                fp.write(stu.name + ',')
                fp.write(str(stu.chinese) + ',')
                fp.write(str(stu.math) + ',')
                fp.write(str(stu.english) + '\n')
            print("导出完毕")

    def scoreavg(self):
        # 求课程平均分
        length = len(self.stulist)
        if length > 0:
            chinese_avg = sum([stu.chinese for stu in self.stulist]) / length
            math_avg = sum([stu.math for stu in self.stulist]) / length
            english_avg = sum([stu.english for stu in self.stulist]) / length
            print('语文成绩平均分是:%.2f' % chinese_avg)
            print('数学成绩平均分是:%.2f' % math_avg)
            print('英语成绩平均分是:%.2f' % english_avg)
        else:
            print('尚没有学生成绩...')

    def scoremax(self):
        # 求课程最高分
        if len(self.stulist) > 0:
            chinese_max = max([stu.chinese for stu in self.stulist])
            math_max = max([stu.math for stu in self.stulist])
            english_max = max([stu.english for stu in self.stulist])
            print('语文成绩最高分是:%d' % chinese_max)
            print('数学成绩最高分是:%d' % math_max)
            print('英语成绩最高分是:%d' % english_max)
        else:
            print('尚没有学生成绩...')

    def scoremin(self):
        # 求课程最低分
        if len(self.stulist) > 0:
            chinese_min = min([stu.chinese for stu in self.stulist])
            math_min = min([stu.math for stu in self.stulist])
            english_min = min([stu.english for stu in self.stulist])
            print('语文成绩最低分是:%d' % chinese_min)
            print('数学成绩最低分是:%d' % math_min)
            print('英语成绩最低分是:%d' % english_min)
        else:
            print('尚没有学生成绩...')

    def infoprocess(self):
        # 基本信息管理
        print('学生基本信息管理'.center(20, '-'))
        print('load----------导入学生信息')
        print('insert--------添加学生信息')
        print('delete--------删除学生信息')
        print('update--------修改学生信息')
        print('show----------显示学生信息')
        print('save----------导出学生信息')
        print('return--------返回')
        print('-' * 28)
        while True:
            s = input('info>').strip().lower()
            if s == 'load':
                fn = input('请输入要导入的文件名:')
                self.load(fn)
            elif s == 'show':
                self.show()
            elif s == 'insert':
                self.insert()
            elif s == 'delete':
                self.delete()
            elif s == 'update':
                self.update()
            elif s == 'save':
                fn = input('请输入要导出的文件名:')
                self.save(fn)
            elif s == 'return':
                break
            else:
                print('输入错误')

    def scoreprocess(self):
        # 学生成绩统计
        print('学生成绩统计'.center(24, '='))
        print('avg    --------课程平均分')
        print('max    --------课程最高分')
        print('min    --------课程最低分')
        print('return --------返回')
        print(''.center(30, '='))
        while True:
            s = input('score>').strip().lower()
            if s == 'avg':
                self.scoreavg()
            elif s == 'max':
                self.scoremax()
            elif s == 'min':
                self.scoremin()
            elif s == 'return':
                break
            else:
                print('输入错误')

    def main(self):
        # 主控函数
        while True:
            print('学生信息管理系统V1.0'.center(24, '='))
            print('info  -------学生基本信息管理')
            print('score -------学生成绩统计')
            print('exit  -------退出系统')
            print(''.center(32, '='))
            # 去除头尾字符,空白字符(换行，回车，制表符，空格),中间的这些字符不能去除
            s = input('main>').strip().lower()
            if s == 'info':
                self.infoprocess()
            elif s == 'score':
                self.scoreprocess()
            elif s == 'exit':
                break
            else:
                print('输入错误')


if __name__ == '__main__':
    st = StudentList() #创建对象
    st.main() #调用对象里的主控函数
