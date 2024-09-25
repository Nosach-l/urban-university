import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                # print(f'{nickname}, Вы успешно авторизовались!')
                return
            # else:
                # print('ошибка ввода данных')

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f'Пользователь {nickname} уже существует!')
            return
        else:
            self.users.append(User(nickname=nickname, password=password, age=age))
            # print(f'Пользователь {nickname} успешно зарегистрирован!')
            self.log_in(nickname=nickname, password=password)

    def log_out(self):
        self.current_user = None
        # print(f'Вы вышли из системы')

    def add(self, *args):
        for vid in args:
            if isinstance(vid, Video):
                if all(video.title != vid.title for video in self.videos):
                    self.videos.append(vid)
                # else:
                    # print('видео с таким названием уже существует')
            # else:
                # print('Недопустимый формат видео')
    #   print("Видео успешно загружено")

    def get_videos(self, search_word):
        if self.videos:
            video_search_list = []
            for video in self.videos:
                if str(search_word).lower() in video.title.lower():
                    video_search_list.append(video.title)
            return video_search_list

    def watch_video(self, search_title):
        if self.current_user is None:
            print(f'Войдите в аккаунт, чтобы смотреть видео!')
        else:
            for video in self.videos:
                if str(search_title) == video.title:
                    if video.adult_mode is True and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу!')
                        return
                    else:
                        for i in range(video.duration):
                            video.time_now = i
                            print(f'{video.time_now}', end='', flush=True)
                            time.sleep(1)
                        print(' Конец видео')
                        video.time_now = 0
                        return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
