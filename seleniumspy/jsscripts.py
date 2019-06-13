
# -*- coding: utf-8 -*-

"""
seleniumspy.jsscripts
~~~~~~~~~~~~
This file contain JS scripts to be enjected to webdriver
:copyright: (c) 2019 by Yasser.
:license: MIT, see LICENSE for more details.
"""

__all__ = ['js_init', 'js_capture', 'js_async_lsitner', 'js_raw_html']

js_init = {}
js_init['js_init_init_check'] = r'''
if(document.pyspy_html_elem) return;
'''

js_init['js_init_html_elem'] = r'''
document.pyspy_html_elem = function(name) {
  if (document.contentType == 'application/xhtml+xml') {
    return 'x:' + name
  } else {
    return name
  }
}
'''

js_init['js_init_xp_attr_val'] = r'''
document.pyspy_xp_attr_val = function(value) {
  if (value.indexOf("'") < 0) {
    return "'" + value + "'"
  } else if (value.indexOf('"') < 0) {
    return '"' + value + '"'
  } else {
    let result = 'concat('
    let part = ''
    let didReachEndOfValue = false
    while (!didReachEndOfValue) {
      let apos = value.indexOf("'")
      let quot = value.indexOf('"')
      if (apos < 0) {
        result += "'" + value + "'"
        didReachEndOfValue = true
        break
      } else if (quot < 0) {
        result += '"' + value + '"'
        didReachEndOfValue = true
        break
      } else if (quot < apos) {
        part = value.substring(0, apos)
        result += "'" + part + "'"
        value = value.substring(part.length)
      } else {
        part = value.substring(0, quot)
        result += '"' + part + '"'
        value = value.substring(part.length)
      }
      result += ','
    }
    result += ')'
    return result
  }
}
'''

js_init['js_init_find_elem'] = r'''
document.pyspy_find_elem = function(loc) {
  try {
    const locator = parse_locator(loc, true)
    return document.pyspy_find_elem({ [locator.type]: locator.string }, document)
  } catch (error) {
    return null
  }
}
'''

js_init['js_init_xp_precise'] = r'''
document.pyspy_xp_precise = function(xpath, e) {
  if (document.pyspy_find_elem(xpath) != e) {
    let result = e.ownerDocument.evaluate(
      xpath,
      e.ownerDocument,
      null,
      XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
      null
    )
    for (let i = 0, len = result.snapshotLength; i < len; i++) {
      let newPath = 'xpath=(' + xpath + ')[' + (i + 1) + ']'
      if (document.pyspy_find_elem(newPath) == e) {
        return newPath
      }
    }
  }
  return xpath
}
'''

js_init['js_init_generate_ids'] = r'''
document.pyspy_generate_ids = function(elem){
    document.IDs_builder = new Object()
    document.IDs_builder.PATHS = {}

    document.IDs_builder.add = function(name, finder) {
    if (finder){
        this.PATHS[name] = finder
        }
    }
    var jsonParser
    if(Object.toJSON){
        jsonParser = Object.toJSON;
    }
    else{
        jsonParser = JSON.stringify;
    }
    document.IDs_builder.add('id', document.pyspy_find_by_id(elem))
    document.IDs_builder.add('name', document.pyspy_find_by_name(elem))
    document.IDs_builder.add('linkText', document.pyspy_find_by_linkText(elem))
    document.IDs_builder.add('css', document.pyspy_find_by_css(elem))
    document.IDs_builder.add('xpath:link', document.pyspy_find_by_xpath_link(elem))
    document.IDs_builder.add('xpath:img', document.pyspy_find_by_xpath_img(elem))
    
    return jsonParser(document.IDs_builder);
}
'''

js_init['js_init_find_by_id'] = r'''
document.pyspy_find_by_id = function id(elem) {
    if (elem.id) {
        return elem.id
        }
    return null
}
'''

js_init['js_init_find_by_name'] = r'''
document.pyspy_find_by_name = function name(elem) {
  if (elem.name) {
    return elem.name
  }
  return null
}
'''

js_init['js_init_find_by_linkText'] = r'''
document.pyspy_find_by_linkText = function linkText(elem) {
  if (elem.nodeName == 'A') {
    let text = elem.textContent
    if (!text.match(/^\s*$/)) {
      return (
        text.replace(/\xA0/g, ' ').replace(/^\s*(.*?)\s*$/, '$1')
      )
    }
  }
  return null
}
'''

js_init['js_init_find_by_xpath_link'] = r'''
document.pyspy_find_by_xpath_link = function xpath_link(elem) {
  if (elem.nodeName == 'A') {
    let text = elem.textContent
    if (!text.match(/^\s*$/)) {
      return document.pyspy_xp_precise(
        '//' +
          document.pyspy_html_elem('a') +
          "[contains(text(),'" +
          text.replace(/^\s+/, '').replace(/\s+$/, '') +
          "')]",
        elem
      )
    }
  }
  return null
}
'''

js_init['js_init_find_by_xpath_img'] = r'''
document.pyspy_find_by_xpath_img = function xpath_img(elem) {
  if (elem.nodeName == 'IMG') {
    if (elem.alt != '') {
      return document.pyspy_xp_precise(
        '//' +
          document.pyspy_html_elem('img') +
          '[@alt=' +
          document.pyspy_xp_attr_val(elem.alt) +
          ']',
        elem
      )
    } else if (elem.title != '') {
      return document.pyspy_xp_precise(
        '//' +
          document.pyspy_html_elem('img') +
          '[@title=' +
          document.pyspy_xp_attr_val(elem.title) +
          ']',
        elem
      )
    } else if (elem.src != '') {
      return document.pyspy_xp_precise(
        '//' +
          document.pyspy_html_elem('img') +
          '[contains(@src,' +
          document.pyspy_xp_attr_val(elem.src) +
          ')]',
        elem
      )
    }
  }
  return null
}
'''

js_init['js_init_find_by_css'] = r'''
document.pyspy_find_by_css = function css_attr(elem) {
  const dataAttributes = ['data-test', 'data-test-id']
  for (let i = 0; i < dataAttributes.length; i++) {
    const attr = dataAttributes[i]
    const value = elem.getAttribute(attr)
    if (value) {
      return `*[${attr}="${value}"]`
    }
  }
  return null
}
'''

js_init['js_init_mouse_over'] = r'''
document.pyspy_mouse_over = function(e){
    if(e.target == document.documentElement) return
    e.target.addEventListener('click', document.pyspy_prevent_click,false);
    e.target.addEventListener('mousedown', document.pyspy_prevent_click,false);
    e.target.addEventListener('mouseup', document.pyspy_prevent_click,false);
    e.target.addEventListener('submit', document.pyspy_prevent_click,false);
    document.pyspy_last_elem = e.target;
    document.pyspy_border_color = e.target.style.outline;
    document.pyspy_highlight_color = e.target.style.backgroundColor;
    e.target.style.outline = "medium solid green";
    e.target.style.backgroundColor = "#FDFF47";
    document.pyspy_spy_listener =  document.pyspy_generate_ids(e.target);
}
'''

js_init['js_init_cursor'] = r'''
document.pyspy_cursor = document.body.style.cursor;
'''

js_init['js_init_prevent_click'] = r'''
document.pyspy_prevent_click = function(e){
    document.pyspy_spy_listener = "*** spy listner is over ***";
    document.removeEventListener('mouseover', document.pyspy_mouse_over);
    document.removeEventListener('click', document.pyspy_prevent_click,false);
    document.removeEventListener('mousedown', document.pyspy_prevent_click,false);
    document.removeEventListener('mouseup', document.pyspy_prevent_click,false);
    document.removeEventListener('submit', document.pyspy_prevent_click,false);

    e.target.removeEventListener('mouseover', document.pyspy_mouse_over);
    e.target.style.outline = document.pyspy_border_color;
    e.target.style.backgroundColor = document.pyspy_highlight_color;
    document.body.style.cursor =  document.pyspy_cursor;
    if(e.stopPropagation) e.stopPropagation();
    if(e.preventDefault) e.preventDefault();
    if(e.stopImmediatePropagation) e.stopImmediatePropagation();
    return false;
}
'''


js_capture = r'''
document.body.style.cursor = "pointer";
document.pyspy_spy_listener = null;
document.addEventListener('click', document.pyspy_prevent_click,false);
document.addEventListener('mousedown', document.pyspy_prevent_click,false);
document.addEventListener('mouseup', document.pyspy_prevent_click,false);
document.addEventListener('submit', document.pyspy_prevent_click,false);
document.addEventListener('mouseover', document.pyspy_mouse_over, false);
'''

js_async_lsitner = r'''
   var callback = arguments[arguments.length - 1];
   if(!document.pyspy_mouse_over){
        callback('{error:"*** spy listner not running ***"}');
        return;
   }
   var waitForActions = function(){
       if(document.pyspy_spy_listener){
        var response = document.pyspy_spy_listener
        document.pyspy_spy_listener = null;
        callback(response);
       }
       else{
        setTimeout(waitForActions, 50);
       }
   }
   waitForActions();
'''

js_raw_html = r'''
    var callback = arguments[arguments.length - 1];
    callback(document.documentElement.innerHTML);
'''

