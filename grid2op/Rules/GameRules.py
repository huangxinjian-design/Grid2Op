from abc import ABC, abstractmethod
import numpy as np

from grid2op.Exceptions import Grid2OpException
from grid2op.Rules.LegalAction import LegalAction
from grid2op.Rules.AlwaysLegal import AlwaysLegal

import pdb

class GameRules(object):
    """
    Class that defin the rules of the game.

    """
    def __init__(self, legalActClass=AlwaysLegal):
        """

        Parameters
        ----------
        legalActClass: ``type``
            The class that will be used to tell if the actions are legal or not. The class must be given, and not
            an object of this class. It should derived from :class:`LegalAction`.
        """
        if not isinstance(legalActClass, type):
            raise Grid2OpException("Parameter \"legalActClass\" used to build the GameRules should be a type (a class) and not an object (an instance of a class). It is currently \"{}\"".format(type(rewardClass)))

        if not issubclass(legalActClass, LegalAction):
            raise Grid2OpException("Gamerules: legalActClass should be initialize with a class deriving from LegalAction and not {}".format(type(legalActClass)))
        self.legal_action = legalActClass()

    def __call__(self, action, env):
        """
        Says if an action is legal or not.

        Parameters
        ----------
        action: :class:`grid2op.Action.Action`
            The action that need to be tested

        env: :class:`grid2op.Environment.Environment`
            The current used environment.

        Returns
        -------
        res: ``bool``
            Assess if the given action is legal or not. ``True``: the action is legal, ``False`` otherwise

        """
        return self.legal_action(action, env)
