from qtpy.QtWidgets import QLabel

from pyqtschema.widgets.base import SchemaWidgetMixin, state_property


class ConstSchemaWidget(SchemaWidgetMixin, QLabel):

    @state_property
    def state(self):
        return self.const_val
    
    @state.setter
    def state(self, value):
        if value != self.const_val:
            raise ValueError(value)

    def configure(self):
        self.const_val = self.schema["const"]
        self.setText(str(self.const_val))

