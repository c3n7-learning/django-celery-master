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

## Run on django to inspect task

celery inspect active
celery inspect active_queues

## Configuring task prioritization (RabbitMQ)

```python
from dcelery.celery import t1,t2,t3
t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)
t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)
t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)
```

## 29. Passing arguments and returning results from Celery tasks

- pass args and keyword args

```shell
>>> from dcelery.celery import t1
>>> t1.apply_async(args=[5,10], kwargs={"message":"The sum is"})
>>> result = t1.apply_async(args=[5,15], kwargs={"message":"The sum is"})
>>> print(result.get())
The sum is: 20
```

#### Async Result

- isCompleted(): Checks whether the task associated with AsyncResult is completed
- isSuccessful(): Checks whether the task completed successfully.
- get(): Blocks the current thread until the task completes.
- getResult(): Returns if task has completed successfully.
- getException(): Returns the exception or error.
