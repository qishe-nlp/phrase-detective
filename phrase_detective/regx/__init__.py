"""Regular Expression used to analyze phrases

.. code:: python

  from phrase_detective.regx import REGX

  print(REGX)
"""

from .en import EN_VERB 
from .es import ES_VERB
from .de import DE_VERB

REGX = {
  "en": EN_VERB,
  "es": ES_VERB,
  "de": DE_VERB,
}
