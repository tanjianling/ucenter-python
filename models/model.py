# -*- coding: utf-8 -*-
import web


class Model(object):
    def __init__(self):
        try:
            self.db = web.database(dbn='mysql', db='test', user='root', pw='root')
        except Exception, e:
            print 'mysql connect error:' + e.__str__()

    def __setattr__(self, key, value):
        return super.__setattr__(self, key, value)

    buildData = {}

    # 构造模型数据属性
    def _buildData(self, data=None):
        _filterField = self._filterProperty()
        if data is not None:
            if isinstance(data, dict):
                self.buildData = data
        elif hasattr(self, 'attributes'):
            if isinstance(self.attributes, dict):
                self.buildData = self.attributes
        elif _filterField:
            for _fieldName in _filterField:
                exec '_fieldValue=self.%s' % (_fieldName)
                self.buildData[_fieldName] = _fieldValue

    # 初始化验证信息
    validateError = {}

    # 验证过滤器
    def _filterValidate(self):
        for _key, _value in self.validateError.items():
            if len(_value) == 0:
                del self.validateError[_key]

    # 验证内置模型
    def _validateValidate(self, field, mode):
        if self.buildData.has_key(field):
            from ucenter.library.validate import Validate
            _validateObj = Validate()
            exec '_callValidate=_validateObj.%s' % (mode)
            if _callValidate(self.buildData[field]) is None:
                self.appendValidateError(field)

    # 验证正则表达式
    def _validateMatch(self, field, matchRule):
        import re
        if self.buildData.has_key(field):
            if re.match(matchRule, self.buildData[field]) is None:
                self.appendValidateError(field)

    # 验证必填项
    def _validateRequired(self, field):
        if self.buildData.has_key(field) == False:
            self.appendValidateError(field)

    # 验证要比较的回调方法
    def _validateCompareMethod(self):
        # 取出规则中的字段
        _ruleField = [x[1] for x in self.rules]
        _existsProperty = compareField = None
        for _property in _ruleField:
            if _property.find('validate') == 0 & hasattr(self, _property):
                _existsProperty = _property
                compareField = _existsProperty.split('_')
                compareField = compareField[len(compareField) - 1]
                if _existsProperty:
                    exec '_callMethod=self.%s' % (_existsProperty)
                    _field = self.rules[_ruleField.index(_existsProperty)][0]
                    _callMethod({
                        _field: self.buildData.get(_field)
                    }, {
                        compareField: self.buildData.get(compareField)
                    })

    # 初始化错误信息项
    def _initValidateErrorMap(self, rules):
        for _rule in rules:
            if _rule[0].find(',') != -1:
                for _field in _rule[0].split(','):
                    _field = _field.strip()
                    self.validateError[_field] = []
            else:
                _field = _rule[0].strip()
                self.validateError[_field] = []

    # 过滤model属性是否属于property
    def _filterProperty(self):
        _dbFields = []
        if hasattr(self, 'property'):
            for _property, value in self.__dict__.items():
                _dbFields.append(_property)
        return _dbFields

    def appendValidateError(self, field):
        _msg = None
        for _field in [x for x in self.rules]:
            if _field[0].find(',') != -1:
                for _f in _field[0].split(','):
                    _f = _f.strip()
                    if _f == field:
                        for _item in _field:
                            if isinstance(_item, dict):
                                _msg = (_item.get('msg') % (_item.get('name')))
                                self.validateError[_f].append(_msg)
            else:
                if _field[0] == field:
                    for _item in _field:
                        if isinstance(_item, dict):
                            _msg = (_item.get('msg') % (_item.get('name')))
                            self.validateError[_field[0]].append(_msg)

    # 触发模型验证
    def validate(self, data=None):
        self._buildData(data)
        if hasattr(self, 'rules'):
            self._initValidateErrorMap(self.rules)
            from ucenter.library.validate import Validate
            for _rule in self.rules:
                _field = _rule[0].strip()
                if 'required' in _rule:
                    if _field != -1:
                        for _field in _rule[0].split(','):
                            self._validateRequired(_field.strip())
                    else:
                        self._validateRequired(_field)
                elif 'match' in _rule:
                    _matchRuleIndex = _rule.index('match') + 1
                    if _rule[_matchRuleIndex] is not None:
                        self._validateMatch(_field, _rule[_matchRuleIndex])
                else:
                    for _item in _rule[1:]:
                        if isinstance(_item, str):
                            if hasattr(Validate, _item):
                                self._validateValidate(_field, _item)
            self._validateCompareMethod()
        self._filterValidate()
