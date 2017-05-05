from libs import globs as gl
class WestKingdom:

    def listify(param):
        cols = gl.cols
        for col in param:
            cols[col] = param[col].tolist()
        return cols

    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d