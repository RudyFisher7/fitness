
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_app/exercise/exercise_list_view.dart';
import 'package:go_router/go_router.dart';

class ExerciseForm extends StatefulWidget {
  const ExerciseForm({super.key});

  @override
  State<StatefulWidget> createState() => _ExerciseFormState();
  
}

class _ExerciseFormState extends State {
  String value = 'text1';
  final List<String> options = ['text1', 'text2', 'text3'];

  @override
  Widget build(BuildContext context) => Center(
    child: Column(
      mainAxisAlignment: MainAxisAlignment.start,
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        ElevatedButton(onPressed: () => context.push('/exercise_list'), child: Text('Choose Exercise')),
        DropdownButton<String>(
          value: value,
          items: options.map((String val) {
            return DropdownMenuItem(value: val, child: Text(val));
          }).toList(),
          onChanged: (String? newValue) => {
            setState(() {
              value = newValue ?? 'text1';
            })
          },
        ),
        Row(
          children: [
            Text('text'),
            Text('text'),
            Text('text'),
            SizedBox(
              width: 140,
              child: TextFormField(
                decoration: InputDecoration(labelText: 'input here'),
                keyboardType: TextInputType.number,
                inputFormatters: [
                  FilteringTextInputFormatter.digitsOnly,
                ],
                validator: (value) {
                  return null;
                },
              ),
            ),
          ],
        ),
      ],
    ),
  );
  
}