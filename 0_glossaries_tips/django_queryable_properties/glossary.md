# Glossary

___

## Liens utiles
[W3School - link](https://www.w3schools.com/django/django_queryset_orderby.php)

## Sommaire
- [Glossary](#glossary)
  - [Liens utiles](#liens-utiles)
  - [Sommaire](#sommaire)
  - [Introduction](#introduction)
  - [Field lookups](#field-lookups)
    - [ORDER BY](#order-by)
    - [DESCENDING ORDER](#descending-order)
    - [Multiple Order Bys](#multiple-order-bys)
  - [Field Lookups Reference](#field-lookups-reference)
  - [Basic queryset filter](#basic-queryset-filter)


---
---

## Introduction
[Sommaire](#sommaire)

**In both cases, the function/method to implement takes 3 arguments:**

`cls` :
The model class. Mainly useful to implement custom logic in inheritance scenarios

`lookup` : 
Used for the filter as a string (e.g. `lt` or `contains`). If a filter call is made without an explicit lookup for an equality comparison
(e.g. via `ApplicationVersion.objects.filter(version_str='2.0')`), the lookup will be `exact`.
If a filter call is made with multiple lookups/transforms (like `field__year__gt` for a date field), the lookup will be the combined string of all
lookups/transforms (`year__gt` for the date example).

`value`:
The value to filter by.

*Using either approach, the function/method is expected to return a Q object that contains the correct filter conditions to represent filtering by the queryable property using the given lookup and value.*

The attribute path specified as the first parameter can not only be a simple field name like in the example above, but also a more complex path to an attribute using dot-notation - basically the same way as for Python’s `operator.attrgetter`. For queryset operations, the dots are then simply replaced by the lookup separator `(__)`, so an attribute path `my.attr` becomes `my__attr` in queries.

a `DateField` may be defined as `date_field = models.DateField()`, which would allow a `ValueCheckProperty` to be set up with the path `date_field.year`. This works because the date object has an attribute `year` on the object-level and Django offers a year transform for querysets `(so date_field__year does in fact work)`.

---
---

## Field lookups
[Sommaire](#sommaire)

`mydata = Members.objects.filter(firstname__in=['Tobias', 'Linus', 'John']).values()`

The in lookup is used to get records where the value is one of the values in an iterable (list, tuple, string, queryset).
The in lookup is case sensitive.

The SQL equivalent to the example above will be:
`WHERE firstname IN ('Tobias', 'Linus', 'John');`


All Field lookup keywords must be specified with the fieldname, followed by two(!) underscore characters __ and the keyword:
`fieldname__in=[value1,value2,value3,...]`

---

**Django has its own way of specifying SQL statements and WHERE clauses. To make specific where clasuses in Django, use "Field lookups". Field lookups are keywords that represents specific SQL keywords.**

*example*
```python
.filter(firstname__startswith='L');
```
*Is the same as the sql statment*
```sql
WHERE firstname LIKE '%L'
```
*The above statement will return records where firstname starts with 'L'.*

---

### ORDER BY
**To sort QuerySets, Django uses the order_by() method:**
*Order the the result alphabetically by firstname:*
```python
mydata = Members.objects.all().order_by('firstname').values()
```

*In SQL, the above statement would be written like this:*
```sql
SELECT * FROM members ORDER BY firstname;
```

---

### DESCENDING ORDER
**By default, the result is sorted ascending (the lowest value first), to change the direction to descending (the highest value first), use the minus sign (NOT), - in front of the field name:**
*Order the the result firstname descending:*
```python
mydata = Members.objects.all().order_by('-firstname').values()
```

*In SQL, the statement would be written like this:*
```sql
SELECT * FROM members ORDER BY firstname DESC;
```

---

### Multiple Order Bys
**To order by more than one field, separate the fieldnames with a comma in the order_by() method:**
*Order the the result first by lastname ascending, then descending on id:*
```python
mydata = Members.objects.all().order_by('lastname', '-id').values()
```

*In SQL, the statement would be written like this:*
```sql
SELECT * FROM members ORDER BY lastname ASC, id DESC;
```

---
---

## Field Lookups Reference
[Sommaire](#sommaire)

Keyword	                |           Description                             |
:----------------------:|:-------------------------------------------------:|
**contains**	        |Contains the phrase                                |
**icontains**	        |Same as contains, but case-insensitive             |
**date**	            |Matches a date                                     |
**day**	                |Matches a date (day of month, 1-31) (for dates)    |
**endswith**	        |Ends with                                          |
**iendswith**	        |Same as endswidth, but case-insensitive            |
**exact**	            |An exact match                                     |
**iexact**	            |Same as exact, but case-insensitive                |
**in**	                |Matches one of the values                          |
**isnull**	            |Matches NULL values                                |
**gt**	                |Greater than                                       |
**gte**	                |Greater than, or equal to                          |
**hour**	            |Matches an hour (for datetimes)                    |
**lt**	                |Less than                                          |
**lte**	                |Less than, or equal to                             |
**minute**	            |Matches a minute (for datetimes)                   |
**month**	            |Matches a month (for dates)                        |
**quarter**	            |Matches a quarter of the year (1-4) (for dates)    |
**range**	            |Match between                                      |
**regex**	            |Matches a regular expression                       |
**iregex**	            |Same as regex, but case-insensitive                |
**second**	            |Matches a second (for datetimes)                   |
**startswith**	        |Starts with                                        |
**istartswith**	        |Same as startswith, but case-insensitive           |
**time**	            |Matches a time (for datetimes)                     |
**week**	            |Matches a week number (1-53) (for dates)           |
**week_day**	        |Matches a day of week (1-7) 1 is sunday            |
**iso_week_day**	    |Matches a ISO 8601 day of week (1-7) 1 is monday   |
**year**	            |Matches a year (for dates)                         |
**iso_year**	        |Matches an ISO 8601 year (for dates)               |

---
---

## Basic queryset filter

*Return only the records where the firstname is 'Emil':*
```python
mydata = Members.objects.filter(firstname='Emil').values()
```

*In SQL, the above statement would be written like this:*
```sql
SELECT * FROM members WHERE firstname = 'Emil';
```

---

**The filter() method takes the arguments as `**kwargs` (keyword arguments), so you can filter on more than one field by sepearting them by a comma.**
*Return records where lastname is "Refsnes" and id is 2:*
```python
mydata = Members.objects.filter(lastname='Refsnes', id=2).values()
```

*In SQL, the above statement would be written like this:*
```sql
SELECT * FROM members WHERE   lastname = 'Refsnes' AND id = 2;
```

---

**We can use multiple filter() methods, separated by a pipe | character. The results will merge into one model.**
*Return records where firstname is either "Emil" or Tobias":*
```python
mydata = Members.objects.filter(firstname='Emil').values() | Members.objects.filter(firstname='Tobias').values()
```

---

**Another common method is to import and use Q expressions:**
*Return records where firstname is either "Emil" or Tobias":*

```python
from django.http import HttpResponse
from django.template import loader
from .models import Members
from django.db.models import Q

def testing(request):
  mydata = Members.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
```

---

*In SQL, the above statement would be written like this:*
```sql
SELECT * FROM members WHERE   firstname = 'Emil' OR firstname = 'Tobias';
```