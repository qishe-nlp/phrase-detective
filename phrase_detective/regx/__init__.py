"""Regular Expression used to analyze phrases

.. code:: python

  from phrase_detective.regx import REGX

  print(REGX)
"""

from .en import en_regx
from .es import es_regx

REGX = {
  "en": en_regx,
  "es": es_regx,
}
