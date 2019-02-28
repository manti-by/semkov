from wagtail.admin.rich_text.converters.editor_html import WhitelistRule
from wagtail.core import hooks
from wagtail.core.whitelist import allow_without_attributes, attribute_rule


@hooks.register('register_rich_text_features')
def register_blockquote_feature(features):
    features.register_converter_rule('editorhtml', 'table', [
        WhitelistRule('table', allow_without_attributes)
    ])
    features.register_converter_rule('editorhtml', 'thead', [
        WhitelistRule('thead', allow_without_attributes),
    ])
    features.register_converter_rule('editorhtml', 'tbody', [
        WhitelistRule('tbody', allow_without_attributes),
    ])
    features.register_converter_rule('editorhtml', 'tr', [
        WhitelistRule('tr', allow_without_attributes),
    ])
    features.register_converter_rule('editorhtml', 'th', [
        WhitelistRule('th', allow_without_attributes),
    ])
    features.register_converter_rule('editorhtml', 'td', [
        WhitelistRule('td', allow_without_attributes),
    ])
