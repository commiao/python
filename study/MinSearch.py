class GridSearch():
    """
    网格点搜索。初始化时需要提供：
    search_range：搜索范围，一个列表或者元组(-1,1) (1,-1)
    n：           网格点数量
    使用时重载GridSearch.f
    """

    def __init__(self, search_range, n):
        from math import inf
        self.lb, self.ub = min(search_range), max(search_range)
        self.n = n
        self.min = inf
        self.argx = inf

    # 需要被最小化的函数
    def f(self, x):
        pass

    def search(self):
        for i in range(self.n):
            x = self.lb + (self.ub - self.lb)/(self.n-1)*i
            fv = self.f(x)
            if self.min > fv:
                self.min = fv
                self.argx = x


searcher = GridSearch([-1,1], 100)
searcher.f = lambda x: x**2
searcher.search()
print("x=%s时取得最小值%s" % (searcher.argx, searcher.min))

