## task 5
# class Person:
#     __iteration_list = ('fio', 'job', 'old', 'salary', 'year_job')

#     def __init__(self, fio, job, old, salary, year_job):
#         self.fio = fio
#         self.job = job
#         self.old = old
#         self.salary = salary
#         self.year_job = year_job
#         self.iteration_step = 0

#     def __getitem__(self, idx):
#         try:
#             return getattr(self, self.__iteration_list[idx])
#         except (IndexError, TypeError):
#             raise IndexError('неверный индекс')

#     def __setitem__(self, idx, value):
#         try:
#             setattr(self, self.__iteration_list[idx], value)
#         except (IndexError, TypeError):
#             raise IndexError('неверный индекс')

#     def __iter__(self):
#         self.iteration_step = 0
#         return self

#     def __next__(self):
#         try:
#             next_value = self[self.iteration_step]
#             self.iteration_step += 1
#             return next_value
#         except IndexError:
#             raise StopIteration




# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# #pers.fio = 1

# for i in pers:
#     print(i)