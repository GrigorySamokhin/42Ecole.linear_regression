
### ft_linear_regression @ 42 Ecole

#### Usage

##### 1. Train model:
```
  python train.py
```
##### 2. Evaluate model:

```
  python evaluate.py
```

##### 3. Visualization

Visualizate regression line while training
```
  python train.py --visu on
```

Visualizate regression line after training

```
  python train.py --visu last
```

Visualizate data
```
  python train.py --visu last
```

Visualizate MSE curve

```
  python train.py --visu mse
```
##### 4. Metrics

Print MSE every 10000 cicles
```
  python train.py --metric mse
```
