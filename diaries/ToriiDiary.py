from diaries.AbstractDiary import AbstractDiary
class ToriiDiary(AbstractDiary):
    def get_date(self):
        return "2024-11-28"
    def get_summary(self):
        return """今日のオブジェクト指向プログラミング及び演習２では、GitHubを用いたチーム開発について学習した。これまでGitHubを使ったことはあったが、この授業を機に基礎の理解をより深めたいと思う。"""
    def get_author(self):
        return "Torii"