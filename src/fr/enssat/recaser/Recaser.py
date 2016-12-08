from src.fr.enssat.recaser import RecaserMethod
from src.fr.enssat.recaser.validation.Restorator import Restorator


class Recaser(object) :

    @staticmethod
    def recase(text_query, approach):
        """Recase the given text_query using the given approach."""

        #if approach not in RecaserMethod.__members__.items():
        #    raise Exception("Invalid approach !")

        restorator = Restorator()
        result = restorator.restore(text_query, approach)

        print("----- RECASER USING: ", approach)
        print("Query  = ", text_query)
        print("Result = ", result)

        #TODO: Add measures