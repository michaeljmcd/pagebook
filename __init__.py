from calibre.customize import InterfaceActionBase

class PageBook(InterfaceActionBase):
  name = 'Pagebook'
  description = 'A plugin to convert a list of one or more URLs to an ebook.'
  supported_platforms = ['windows', 'osx', 'linux']
  author = 'Michael McDermott
  version = (1, 0, 0)
  minimum_calibre_version = (0, 7, 53)

  actual_plugin = 'calibre_plugins.pagebook.ui:PageBookPlugin'

  def is_customizable(self):
    return False
