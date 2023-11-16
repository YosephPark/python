class Television:
    '''
    A class representing details for tv object
    4 class variables as follows:
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self) -> None:
        '''
        Constructor to create initial state of tv object
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        Method to toggle the tv on/off status
        '''
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        '''
        Method to toggle the tv mute state
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True
        else:
            pass

    def channel_up(self) -> None:
        '''
        Method to increase the tv channel
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        Method to decrease the tv channel
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        Method to increase the tv volume
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        '''
        Method to decrease the tv volume
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        '''
        Method to show the tv status
        :return: tv state
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

