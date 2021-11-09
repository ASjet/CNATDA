import sys
from time import time
HEADER_SIZE = 12

class RtpPacket:
    header = bytearray(HEADER_SIZE)

    def __init__(self):
        pass

    def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
        """Encode the RTP packet with header fields and payload."""
        timestamp = int(time())
        header = bytearray(HEADER_SIZE)
        #--------------
        # TO COMPLETE
        #--------------
        # Fill the header bytearray with RTP header fields
        V = (int(version) & 0x03) << 6
        P = (int(padding) & 0x01) << 5
        X = (int(extension) & 0x01) << 4
        CC = int(cc) & 0x0F
        header[0] = V | P | X | CC
        M = (int(marker) & 0x01) << 7
        PT = int(pt) & 0x7F
        header[1] = M | PT
        header[2] = (int(seqnum) & 0xFF00) >> 8
        header[3] = int(seqnum) & 0x00FF
        header[4] = (timestamp & 0xFF000000) >> 24
        header[5] = (timestamp & 0x00FF0000) >> 16
        header[6] = (timestamp & 0x0000FF00) >> 8
        header[7] = timestamp & 0x000000FF
        header[8] = (int(ssrc) & 0xFF000000) >> 24
        header[9] = (int(ssrc) & 0x00FF0000) >> 16
        header[10] = (int(ssrc) & 0x0000FF00) >> 8
        header[11] = int(ssrc) & 0x000000FF

        self.header = header

        # Get the payload from the argument
        self.payload = payload

    def decode(self, byteStream):
        """Decode the RTP packet."""
        self.header = bytearray(byteStream[:HEADER_SIZE])
        self.payload = byteStream[HEADER_SIZE:]

    def version(self):
        """Return RTP version."""
        return int(self.header[0] >> 6)

    def seqNum(self):
        """Return sequence (frame) number."""
        seqNum = self.header[2] << 8 | self.header[3]
        return int(seqNum)

    def timestamp(self):
        """Return timestamp."""
        timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
        return int(timestamp)

    def payloadType(self):
        """Return payload type."""
        pt = self.header[1] & 127 # 0111 1111
        return int(pt)

    def getPayload(self):
        """Return payload."""
        return self.payload

    def getPacket(self):
        """Return RTP packet."""
        return self.header + self.payload