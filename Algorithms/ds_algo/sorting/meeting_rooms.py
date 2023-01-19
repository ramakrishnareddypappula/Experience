
# a = [[s1, e1], [s2, e2], [s3, e3]] Can a person attend all the meetings?


# Time = O(n log n) sort by 0th index. Compare 1st index of current element with 0th index of next element. so on.
def meeting_rooms(meeting_times):
    meeting_times.sort(key=lambda var: var[0])
    for i in range(len(meeting_times) - 1):
        if meeting_times[i][1] > meeting_times[i + 1][0]:
            return 0
    return 1



print(meeting_rooms([[0,30],[15,20],[5,10]]))
print(meeting_rooms([[7,10],[2, 4]]))
print(meeting_rooms([[1,4],[5, 9], [10, 12]]))
print(meeting_rooms([[1,4],[5, 11], [10, 12]]))