
### ft_linear_regression @ 42 Ecole

#### Usage

##### 1. Train model:
```python
python train.py
```
##### 2. Evaluate model:

```python
python evaluate.py
```

##### 3. Visualization

Visualizate regression line while training
```python
python train.py --visu on
```

Visualizate regression line after training

```python
python train.py --visu last
```

Visualizate data
```python
python train.py --visu last
```

Visualizate MSE curve

```python
python train.py --visu mse
```

##### 4. Metrics

Print MSE every 10000 cicles
```python
pythin train.py --metric mse
```
