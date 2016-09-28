params = input().split()
n = int(params[0])
m = int(params[1])
k = int(params[2])

if k > 0:
    tracks = []
    for i in range(k):
        trackStr = input().split()
        row = int(trackStr[0])
        column1 = int(trackStr[1])
        column2 = int(trackStr[2])
        tracks.append((row, column1, column2))

    tracks.sort()

    totalTrackLength = 0
    currentRow = tracks[0][0]
    currentColumn = 0
    for track in tracks:
        # print(track)
        if track[0] == currentRow:
            if currentColumn < track[1]:
                totalTrackLength += (track[2] - track[1] + 1)
                currentColumn = track[2]
            elif currentColumn < track[2]:
                totalTrackLength += track[2] - currentColumn
                currentColumn = track[2]
        else:
            currentRow = track[0]
            currentColumn = track[2]
            totalTrackLength += (track[2] - track[1] + 1)
        # print(totalTrackLength)

    lampposts = n*m - totalTrackLength
    print(lampposts)
else:
    print(n*m)
