import pygame, random, os

#seek for the knight.
def wknightseek(objectfs,tiles):
    objectfs.available = []
    objectfs.seekx = objectfs.tilex
    objectfs.seeky = objectfs.tiley
    objectfs.seektile = objectfs.tile

    objectfs.seekx += 2
    objectfs.seeky += 1
    objectfs.seektile = 'x' + str(objectfs.seekx)+ 'y'+str(objectfs.seeky)
    for tile in tiles:
        if tile.name == objectfs.seektile:
            objectfs.seektile = tile.name
            objectfs.available.append(objectfs.seektile)

    objectfs.seekx = objectfs.tilex
    objectfs.seeky = objectfs.tiley
    objectfs.seektile = objectfs.tile
    objectfs.seekx += 1
    objectfs.seeky += 2
    objectfs.seektile = 'x' + str(objectfs.seekx)+ 'y'+str(objectfs.seeky)
    for tile in tiles:
        if tile.name == objectfs.seektile:
            objectfs.seektile = tile.name
            for peice in objectfs.team:
                if peice.name is not objectfs.name and peice.tile == tile.name:
                    objectfs.available.append(objectfs.seektile)
    objectfs.seekx = objectfs.tilex
    objectfs.seeky = objectfs.tiley
    objectfs.seektile = objectfs.tile
    objectfs.seekx += -2
    objectfs.seeky += -1
    objectfs.seektile = 'x' + str(objectfs.seekx)+ 'y'+str(objectfs.seeky)
    for tile in tiles:
        if tile.name == objectfs.seektile:
            objectfs.seektile = tile.name
            objectfs.available.append(objectfs.seektile)
    objectfs.seekx = objectfs.tilex
    objectfs.seeky = objectfs.tiley
    objectfs.seektile = objectfs.tile

    objectfs.seekx += -1
    objectfs.seeky += -2
    objectfs.seektile = 'x' + str(objectfs.seekx)+ 'y'+str(objectfs.seeky)
    for tile in tiles:
        if tile.name == objectfs.seektile:
            objectfs.seektile = tile.name
            objectfs.available.append(objectfs.seektile)

    objectfs.seekx = objectfs.tilex
    objectfs.seeky = objectfs.tiley
    objectfs.seektile = objectfs.tile
    objectfs.seekx += 1
    objectfs.seeky += -2
    objectfs.seektile = 'x' + str(objectfs.seekx)+ 'y'+str(objectfs.seeky)
    for tile in tiles:
        if tile.name == objectfs.seektile:
            objectfs.seektile = tile.name
            objectfs.available.append(objectfs.seektile)
    objectfs.seekx = objectfs.tilex
    objectfs.seeky = objectfs.tiley
    objectfs.seektile = objectfs.tile
    objectfs.seekx += -1
    objectfs.seeky += 2
    objectfs.seektile = 'x' + str(objectfs.seekx)+ 'y'+str(objectfs.seeky)
    for tile in tiles:
        if tile.name == objectfs.seektile:
                objectfs.seektile = tile.name
                objectfs.available.append(objectfs.seektile)
    objectfs.seekx = objectfs.tilex
    objectfs.seeky = objectfs.tiley
    objectfs.seektile = objectfs.tile
    objectfs.seekx += 2
    objectfs.seeky += -1
    objectfs.seektile = 'x' + str(objectfs.seekx)+ 'y'+str(objectfs.seeky)
    for tile in tiles:
        if tile.name == objectfs.seektile:
            objectfs.seektile = tile.name
            objectfs.available.append(objectfs.seektile)
    objectfs.seekx = objectfs.tilex
    objectfs.seeky = objectfs.tiley
    objectfs.seektile = objectfs.tile
    objectfs.seekx += -2
    objectfs.seeky += 1
    objectfs.seektile = 'x' + str(objectfs.seekx)+ 'y'+str(objectfs.seeky)
    objectfs.seekx = objectfs.tilex
    objectfs.seeky = objectfs.tiley
    objectfs.seektile = objectfs.tile
    objectfs.seekx += -2
    objectfs.seeky += 1
    objectfs.seektile = 'x' + str(objectfs.seekx)+ 'y'+str(objectfs.seeky)
    for tile in tiles:
        if tile.name == objectfs.seektile:
            objectfs.seektile = tile.name
            objectfs.available.append(objectfs.seektile)
    objectfs.seekx = objectfs.tilex
    objectfs.seeky = objectfs.tiley
    objectfs.seektile = objectfs.tile
    objectfs.seekx += 1
    objectfs.seeky += 2
    objectfs.seektile = 'x' + str(objectfs.seekx)+ 'y'+str(objectfs.seeky)
    for tile in tiles:
        if tile.name == objectfs.seektile:
            objectfs.seektile = tile.name
            objectfs.available.append(objectfs.seektile)


    return objectfs.available
