import barcode

class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        tag = barcode.barcode(product_code, writer=barcode.barcode())
        path_from_tag = f'{tag}'
        tag.save(path_from_tag)

        return path_from_tag