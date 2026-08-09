import Foundation
import Darwin
import Translation

private struct TranslationInput: Decodable {
    let texts: [String]
    let batchSize: Int?
}

private struct TranslationOutput: Encodable {
    let translations: [String]
}

@main
private struct AppleTranslator {
    static func main() async throws {
        let inputData = FileHandle.standardInput.readDataToEndOfFile()
        let input = try JSONDecoder().decode(TranslationInput.self, from: inputData)
        let source = Locale.Language(identifier: "zh-Hans")
        let target = Locale.Language(identifier: "en")
        let availability = LanguageAvailability()
        let status = await availability.status(from: source, to: target)

        guard status == .installed else {
            FileHandle.standardError.write(
                Data("Chinese-to-English translation languages are not installed.\n".utf8)
            )
            exit(2)
        }

        let session = TranslationSession(
            installedSource: source,
            target: target,
            preferredStrategy: .highFidelity
        )

        let batchSize = max(1, min(input.batchSize ?? 96, 256))
        var translated: [String] = []
        translated.reserveCapacity(input.texts.count)

        var start = 0
        while start < input.texts.count {
            let end = min(start + batchSize, input.texts.count)
            let requests = input.texts[start..<end].enumerated().map { offset, text in
                TranslationSession.Request(
                    sourceText: text,
                    clientIdentifier: String(start + offset)
                )
            }
            let responses = try await session.translations(from: requests)
            translated.append(contentsOf: responses.map(\.targetText))
            start = end
            FileHandle.standardError.write(
                Data("Translated \(start)/\(input.texts.count) segments\n".utf8)
            )
        }

        let output = TranslationOutput(translations: translated)
        let outputData = try JSONEncoder().encode(output)
        FileHandle.standardOutput.write(outputData)
    }
}
