def get_group_presence(group, dataframe, plot=False):
    try:
        percent = dataframe[group] / dataframe['VAP']
        return percent
    except ZeroDivisionError:
        percent = 0
        return percent