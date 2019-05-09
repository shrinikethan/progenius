class VideoDataModel:
    def __init__(self, videoID, author, keywords="", fileSize=0, mediaFormat="", closedCaption="", contentData="", videoFileName="", cloudProviderModel=None, isDownloadedToServer=0):
        self.videoID = videoID
        self.author = author
        self.keywords = keywords
        self.fileSize = fileSize
        self.mediaFormat = mediaFormat
        self.closedCaption = closedCaption
        self.contentData = contentData
        self.videoFileName = videoFileName
        self.cloudProviderModel = cloudProviderModel
        self.isDownloadedToServer = isDownloadedToServer
