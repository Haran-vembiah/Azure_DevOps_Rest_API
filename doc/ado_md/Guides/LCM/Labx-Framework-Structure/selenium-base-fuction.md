Need to import get_driver from seleniumbase:

**from seleniumbase import get_driver**

To launch desired browser we need to use get_driver function:

**driver = get_driver("chrome", headless=False)**		

**driver = get_driver("firefox", headless=False)**

**driver = get_driver("ie", headless=False)**

To open url we need to use get function:

**driver.get(baseURL)**

**Below are the functions that are used to have action on the webelements:**

Need to import module page_actions from seleniumbase

from seleniumbase import page_actions


**is_element_present(driver, selector, by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”**

**	page_actions.is_element_present()

`    `"""

`    `Returns whether the specified element selector is present on the page.

`    `@Params

`    `driver - the webdriver object (required)

`    `selector - the locator for identifying the page element (required)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `@Returns

`    `Boolean (is element present)

`    `"""


**is_element_visible(driver, selector, by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”**

page_actions.is_element_visible()

`    `"""

`    `Returns whether the specified element selector is visible on the page.

`    `@Params

`    `driver - the webdriver object (required)

`    `selector - the locator for identifying the page element (required)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `@Returns

`    `Boolean (is element visible)

`    `"""


**is_element_enabled(driver, selector, by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”**

page_actions.is_element_enabled()

`    `"""

`    `Returns whether the specified element selector is enabled on the page.

`    `@Params

`    `driver - the webdriver object (required)

`    `selector - the locator for identifying the page element (required)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `@Returns

`    `Boolean (is element enabled)

`    `"""


**is_text_visible(driver, text, selector, by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”**

page_actions.is_text_visible()

`    `"""

`    `Returns whether the specified text is visible in the specified selector.

`    `@Params

`    `driver - the webdriver object (required)

`    `text - the text string to search for

`    `selector - the locator for identifying the page element (required)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `@Returns

`    `Boolean (is text visible)

`    `"""


**is_attribute_present(**

`    `**driver, selector, attribute, value=None, by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”**

page_actions.is_attribute_present()

`    `"""

`    `Returns whether the specified attribute is present in the given selector.

`    `@Params

`    `driver - the webdriver object (required)

`    `selector - the locator for identifying the page element (required)

`    `attribute - the attribute that is expected for the element (required)

`    `value - the attribute value that is expected (Default: None)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `@Returns

`    `Boolean (is attribute present)

`    `"""


**wait_for_element_present(**

`    `**driver,**

`    `**selector,**

`    `**by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”,**

`    `**timeout=settings.LARGE_TIMEOUT,**

`    `**original_selector=None,**

page_actions.wait_for_element_present()

`    `"""

`    `Searches for the specified element by the given selector. Returns the

`    `element object if it exists in the HTML. (The element can be invisible.)

`    `Raises NoSuchElementException if the element does not exist in the HTML

`    `within the specified timeout.

`    `@Params

`    `driver - the webdriver object

`    `selector - the locator for identifying the page element (required)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `timeout - the time to wait for elements in seconds

`    `original_selector - handle pre-converted ":contains(TEXT)" selector

`    `@Returns

`        `A web element object

`    `"""


**wait_for_element_visible(**

`    `**driver,**

`    `**selector,**

`    `**by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”,**

`    `**timeout=settings.LARGE_TIMEOUT,**

`    `**original_selector=None,**


**	page_actions.wait_for_element_visible()

`    `"""

`    `Searches for the specified element by the given selector. Returns the

`    `element object if the element is present and visible on the page.

`    `Raises NoSuchElementException if the element does not exist in the HTML

`    `within the specified timeout.

`    `Raises ElementNotVisibleException if the element exists in the HTML,

`    `but is not visible (eg. opacity is "0") within the specified timeout.

`    `@Params

`    `driver - the webdriver object (required)

`    `selector - the locator for identifying the page element (required)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `timeout - the time to wait for elements in seconds

`    `original_selector - handle pre-converted ":contains(TEXT)" selector

`    `@Returns

`    `A web element object

`    `"""




**wait_for_text_visible(**

`    `**driver,**

`    `**text,**

`    `**selector,**

`    `**by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”,**

`    `**timeout=settings.LARGE_TIMEOUT,**

`    `**browser=None,**


**	page_actions.wait_for_text_visible()

`    `"""

`    `Searches for the specified element by the given selector. Returns the

`    `element object if the text is present in the element and visible

`    `on the page.

`    `Raises NoSuchElementException if the element does not exist in the HTML

`    `within the specified timeout.

`    `Raises ElementNotVisibleException if the element exists in the HTML,

`    `but the text is not visible within the specified timeout.

`    `@Params

`    `driver - the webdriver object (required)

`    `text - the text that is being searched for in the element (required)

`    `selector - the locator for identifying the page element (required)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `timeout - the time to wait for elements in seconds

`    `browser - used to handle a special edge case when using Safari

`    `@Returns

`    `A web element object that contains the text searched for

`    `"""


**wait_for_exact_text_visible(**

`    `**driver,**

`    `**text,**

`    `**selector,**

`    `**by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”,**

`    `**timeout=settings.LARGE_TIMEOUT,**

`    `**browser=None,**


**	page_actions.wait_for_exact_text_visible()

`    `"""

`    `Searches for the specified element by the given selector. Returns the

`    `element object if the text matches exactly with the text in the element,

`    `and the text is visible.

`    `Raises NoSuchElementException if the element does not exist in the HTML

`    `within the specified timeout.

`    `Raises ElementNotVisibleException if the element exists in the HTML,

`    `but the exact text is not visible within the specified timeout.

`    `@Params

`    `driver - the webdriver object (required)

`    `text - the exact text that is expected for the element (required)

`    `selector - the locator for identifying the page element (required)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `timeout - the time to wait for elements in seconds

`    `browser - used to handle a special edge case when using Safari

`    `@Returns

`    `A web element object that contains the text searched for

`    `"""


**wait_for_attribute(**

`    `**driver,**

`    `**selector,**

`    `**attribute,**

`    `**value=None,**

`    `**by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”,**

`    `**timeout=settings.LARGE_TIMEOUT,**


**	page_actions.wait_for_attribute()

`    `"""    Searches for the specified element attribute by the given selector.

`    `Returns the element object if the expected attribute is present

`    `and the expected attribute value is present (if specified).

`    `Raises NoSuchElementException if the element does not exist in the HTML

`    `within the specified timeout.

`    `Raises NoSuchAttributeException if the element exists in the HTML,

`    `but the expected attribute/value is not present within the timeout.

`    `@Params

`    `driver - the webdriver object (required)

`    `selector - the locator for identifying the page element (required)

`    `attribute - the attribute that is expected for the element (required)

`    `value - the attribute value that is expected (Default: None)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `timeout - the time to wait for the element attribute in seconds

`    `@Returns

`    `A web element object that contains the expected attribute/value

`    `"""

**wait_for_element_clickable(**

`    `**driver,**

`    `**selector,**

`    `**by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”,**

`    `**timeout=settings.LARGE_TIMEOUT,**

`    `**original_selector=None,**


**	page_actions.wait_for_element_clickable()



"""

`    `Searches for the specified element by the given selector. Returns the

`    `element object if the element is present, visible, & clickable on the page.

`    `Raises NoSuchElementException if the element does not exist in the HTML

`    `within the specified timeout.

`    `Raises ElementNotVisibleException if the element exists in the HTML,

`    `but is not visible (eg. opacity is "0") within the specified timeout.

`    `Raises ElementNotInteractableException if the element is not clickable.

`    `@Params

`    `driver - the webdriver object (required)

`    `selector - the locator for identifying the page element (required)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `timeout - the time to wait for elements in seconds

`    `original_selector - handle pre-converted ":contains(TEXT)" selector

`    `@Returns

`    `A web element object

`    `"""


**wait_for_element_absent(**

`    `**driver,**

`    `**selector,**

`    `**by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”,**

`    `**timeout=settings.LARGE_TIMEOUT,**

`    `**original_selector=None,**

**	page_actions.wait_for_element_absent()

`    `"""

`    `Searches for the specified element by the given selector.

`    `Raises an exception if the element is still present after the

`    `specified timeout.

`    `@Params

`    `driver - the webdriver object

`    `selector - the locator for identifying the page element (required)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `timeout - the time to wait for elements in seconds

`    `original_selector - handle pre-converted ":contains(TEXT)" selector

`    `"""


**wait_for_element_not_visible(**

`    `**driver,**

`    `**selector,**

`    `**by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”,**

`    `**timeout=settings.LARGE_TIMEOUT,**

`    `**original_selector=None,**


**	page_actions.wait_for_element_not_visible()

`    `"""

`    `Searches for the specified element by the given selector.

`    `Raises an exception if the element is still visible after the

`    `specified timeout.

`    `@Params

`    `driver - the webdriver object (required)

`    `selector - the locator for identifying the page element (required)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `timeout - the time to wait for the element in seconds

`    `original_selector - handle pre-converted ":contains(TEXT)" selector

`    `"""



**find_visible_elements(driver, selector, by=selectortype)  selectortype eg: “id”, “class”, “name”, “xpath”, “css selector”**

page_actions.find_visible_elements()

`    `"""

`    `Finds all WebElements that match a selector and are visible.

`    `Similar to webdriver.find_elements.

`    `@Params

`    `driver - the webdriver object (required)

`    `selector - the locator for identifying the page element (required)

`    `by - the type of selector being used (Default: By.CSS_SELECTOR)

`    `"""


**wait_for_and_accept_alert(driver, timeout=settings.LARGE_TIMEOUT)**

page_actions.wait_for_and_accept_alert()

`    `"""

`    `Wait for and accept an alert. Returns the text from the alert.

`    `@Params

`    `driver - the webdriver object (required)

`    `timeout - the time to wait for the alert in seconds

`    `"""


**wait_for_and_dismiss_alert(driver, timeout=settings.LARGE_TIMEOUT)**

page_actions.wait_for_and_dismiss_alert()



` `"""

`    `Wait for and dismiss an alert. Returns the text from the alert.

`    `@Params

`    `driver - the webdriver object (required)

`    `timeout - the time to wait for the alert in seconds

`    `"""


**wait_for_and_switch_to_alert(driver, timeout=settings.LARGE_TIMEOUT)**

page_actions.wait_for_and_switch_to_alert()

`    `"""

`    `Wait for a browser alert to appear, and switch to it. This should be usable

`    `as a drop-in replacement for driver.switch_to.alert when the alert box

`    `may not exist yet.

`    `@Params

`    `driver - the webdriver object (required)

`    `timeout - the time to wait for the alert in seconds

`    `"""


**switch_to_frame(driver, frame, timeout=settings.SMALL_TIMEOUT)**

page_actions.switch_to_frame()

`    `"""

`    `Wait for an iframe to appear, and switch to it. This should be

`    `usable as a drop-in replacement for driver.switch_to.frame().

`    `@Params

`    `driver - the webdriver object (required)

`    `frame - the frame element, name, id, index, or selector

`    `timeout - the time to wait for the alert in seconds

`    `"""


**switch_to_window(driver, window, timeout=settings.SMALL_TIMEOUT)**

page_actions.switch_to_window()



` `"""    Wait for a window to appear, and switch to it. This should be usable

`    `as a drop-in replacement for driver.switch_to.window().

`    `@Params

`    `driver - the webdriver object (required)

`    `window - the window index or window handle

`    `timeout - the time to wait for the window in seconds

`    `"""
