tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp4.delay()

## Task Grouping

- Allows running of tasks in parallel

```shell
>>> from celery import group
>>> from newapp.tasks import tp1,tp2,tp3,tp4
>>> tasks_group= group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
>>> tasks_group.apply_async()
<GroupResult: 743dec72-35d9-4eba-8d44-29aeaff534d2 [b9d82c5e-5030-477d-b849-3456b1da7773, 9a9d7a7a-a3e9-4e03-a098-139fbca4575d, ae41899d-7bf5-48b4-96ca-ff20521749d2, 3d2f189f-c789-4978-9b3e-929f261f8ab5]>
```

## Task Chaining

- Allows running of tasks one after another

```shell
>>> from newapp.tasks import tp1,tp2,tp3,tp4
>>> from celery import chain
>>> task_chain = chain(tp1.s(),tp2.s(),tp3.s(),tp4.s())
>>> task_chain.apply_async()
<AsyncResult: e14d5975-69a8-4bc6-bbaa-ab3de98c4a68>
```
