django-csv
==========

Some CSV Utilities for your django projects


===========
Basic Usage
===========

1. Import ``django_csv``
2. Create a new ``CSVUtilities`` instance with a single parameter, the path to a CSV file


===========
Main Methods
===========
```
read_csv_into_model(model, csv_indices, delimeter=',', filter_fun=None, after_creation=None, start_row=0, dry_run=False, init_args={})
```
---
Create django model instances from the rows of this ``CSVUtilities`` instance's csv file. Each row of the csv will map to a new model instance unless the row doesn't pass the ``filter_fun`` test.

Arguments:
* ``model`` - the django class to create instances of
* ``csv_indices`` - a dictionary of field names mapped to the column index in the csv which holds the field value
* ``delimiter`` - the csv delimiter
* ``filter_fun`` - a callable which receives the current row in the csv as it's single argument. Return ``True`` for the row to create a new model instance and ``False`` for the row to be skipped. If not provided, will never skip rows.
* ``after_creation`` - a callable which receives two arguments, the (unsaved) model instance and the current csv row. If ``after_creation`` is provided you are responsible for calling ``save()`` to write the instance to the db.
* ``start_row`` - the row in the csv to start reading from
* ``dry_run`` - if ``True``, no model instances will be saved, just the count of the number of model instances that *would* be created will be returned.
* ``init_args`` - dictionary of attributes to set for every created model instance

```
check_pred_against_rows(pred, delimiter=',')
```
---
Get a list of all csv rows that pass the given predicate

Arguments:
* ``pred`` - a callable which receives the current csv row as its single parameter and should return a truthy value
* ``delimiter`` - the csv delimiter

```
csv_from_excel(excel_file, csv_name)
```
Create a csv file from an excel file. 
**Note:** Requires ``xlrd`` package.

Arguments:
* ``excel_file`` - a File object which we'll create the csv file from
* ``csv_name`` - path to the csv file to create (shouldn't include the .csv extension)


===========
Examples
===========
Base Class:
```
class DjangoClass(models.Model):
  name = models.CharField(max_length=200)
  age = models.IntegerField()
```
