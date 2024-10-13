import pickle
import EncodeGenerator
KnownFaces = EncodeGenerator.KnownFaces()
# print(KnownFaces)
def PickleCreation():
    #Store the Registered Faces in Pickle File with IDs
    file = open('PickleFile.p','wb')
    pickle.dump(KnownFaces,file)
    file.close()
    return 'PickleFile.p'


