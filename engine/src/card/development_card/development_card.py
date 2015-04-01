# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from engine.src.resource_type import ResourceType


class DevelopmentCard(object):
    __metaclass__ = ABCMeta

    def __init__(self):

        self.cost = {ResourceType.GRAIN: 1, ResourceType.ORE: 1,
                     ResourceType.WOOL: 1}

        self.played = False
        self.is_playable = True

    def __str__(self):
        return self.__class__.__name__
        
    @abstractmethod
    def draw_card(self, game, player):
        """Draw this card and activate any effect incurred by holding it.
         
         This method should be called only once when purchased by a player.
         
        Args:
            game (Game): The game this card may possibly affect.
            
            player(Player): The player that bought this development card.
        
        Returns:
            None. Should call functions on game and player.
        """
        pass

    @abstractmethod
    def play_card(self, game, player):
        """Draw this card and activate any relevant effect.
         
         This method should be called only once when played by a player.
         
        Args:
            game (Game): The game this card may possibly affect.
            
            player(Player): The player that played this development card.
        
        Returns:
            None. Should call functions on game and player.
        """

        self.played = True