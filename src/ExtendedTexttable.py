import texttable

class ExtendedTexttable(texttable.Texttable):

    FOOTER = 1 << 4

    def footer(self, array):
        """Specify the footer of the table
        """

        self._check_row_size(array)
        self._footer = list(map(texttable.obj2unicode, array))

    def draw(self):
        out = super(ExtendedTexttable, self).draw()

        if self._footer:
            if self._has_border():
                out = self.remove_last_line_from_string(out)
            out += "\n"
            if self._has_footer():
                out += self._hline_header()
            out += self._draw_line(self._footer, isheader=False)

            if self._has_border():
                out += self._hline()

        return out[:-1]
    
    def _has_footer(self):
        """Return a boolean, if header line is required or not
        """

        return self._deco & self.FOOTER > 0
    
    def remove_last_line_from_string(self, s):
        return s[:s.rfind('\n')]